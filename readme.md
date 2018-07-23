# nfsn-pingbot

NFSN pingbot is a tool for updating a DNS A record managed by [NFSN][] to
match the automatically discovered external IP of a host. If you run it on
a cron job, it can basically be used to implement dynamic-dns.

## Building

NFSN pingbot is built using [bazel](https://www.bazel.build/). Once bazel is
installed, you should be able to run:

```bash
$ bazel build :nfsn_pingbot
$ sudo install --mode=0555 bazel-bin/nfsn_pingbot /usr/bin/
```

Then you can invoke the pingbot like so: `nfsn_pingbot --help`. Since bazel
is magic this should work as long as you have a python 2.7 interpreter
installed in a reasonable location. Dependencies are handled automatically.
To remove, run `rm /usr/bin/nfsn_pingbot`.

## Usage

If you want to update the domain `foo.example.com` whenever your IP changes,
add a cron job with the command:

```
nfsn_pingbot <nfsn-user> <path/to/nfsn_api_key> example.com foo
```

[NFSN]: http://nearlyfreespeech.net
