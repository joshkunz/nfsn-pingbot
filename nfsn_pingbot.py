#!/usr/bin/env python

from nfsn import Nfsn
import requests
import logging as log

def current_ip():
    return requests.get("https://httpbin.org/ip").json()["origin"]

def update_if_needed(nfsn, domain, subdomain, ip):
    rrs = nfsn.dns(domain).listRRs(name=subdomain, type="A")
    assert len(rrs) <= 1, "Shouldn't have more than one A record"

    if len(rrs) == 0:
        log.info("Dynamic record does not exist, creating...")
        nfsn.dns(domain).addRR(name=subdomain, type="A", data=ip)
        return

    rr = rrs[0]
    if rr.data == ip:
        return

    log.info("Dynamic ip is {0}, actual ip is {1}, updating...".format(rr.data, ip))
    nfsn.dns(domain).removeRR(name=subdomain, type="A", data=rr.data)
    nfsn.dns(domain).addRR(name=subdomain, type="A", data=ip)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("nfsn_login")
    parser.add_argument("nfsn_api_key_file_path")
    parser.add_argument("domain")
    parser.add_argument("subdomain")
    args = parser.parse_args()

    with open(args.nfsn_api_key_file_path) as keyfile:
        nfsn = Nfsn(login=args.nfsn_login, api_key=keyfile.read())
    update_if_needed(nfsn, args.domain, args.subdomain, current_ip())
