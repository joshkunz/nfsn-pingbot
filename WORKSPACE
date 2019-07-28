load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

git_repository(
    name = "rules_python",
    remote = "https://github.com/bazelbuild/rules_python.git",
    commit = "93d8b0af6d8ca1ee37816a829085d7092b04cc7b",
)

# Only needed for PIP support:
load("@rules_python//python:pip.bzl", "pip_repositories", "pip_import")

pip_repositories()

# Required PIP packages for nfsn-pingbot
pip_import(
   name = "pip_deps",
   requirements = "//:requirements.txt",
)

# Actually load the required pip packages
load("@pip_deps//:requirements.bzl", "pip_install")
pip_install()
