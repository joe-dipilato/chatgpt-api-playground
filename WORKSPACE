load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive", "http_file")

http_archive(
    name = "rules_python",
    sha256 = "497ca47374f48c8b067d786b512ac10a276211810f4a580178ee9b9ad139323a",
    strip_prefix = "rules_python-0.16.1",
    url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.16.1.tar.gz",
)

http_archive(
    name = "bazel_skylib",
    sha256 = "74d544d96f4a5bb630d465ca8bbcfe231e3594e5aae57e1edbf17a6eb3ca2506",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/1.3.0/bazel-skylib-1.3.0.tar.gz",
        "https://github.com/bazelbuild/bazel-skylib/releases/download/1.3.0/bazel-skylib-1.3.0.tar.gz",
    ],
)

PYTHON_VERSION = "3.9.13"

load("@rules_python//python:repositories.bzl", "python_register_toolchains")

python_register_toolchains(
    name = "python3",
    python_version = PYTHON_VERSION,
)

load("@rules_python//python/pip_install:repositories.bzl", "pip_install_dependencies")

pip_install_dependencies()

load("@rules_python//python:pip.bzl", "pip_parse")
load("@python3//:defs.bzl", python_interpreter = "interpreter")

pip_parse(
    name = "pypi",
    enable_implicit_namespace_pkgs = True,
    python_interpreter_target = python_interpreter,
    requirements_linux = "//:requirements_linux.txt",
)

load("@pypi//:requirements.bzl", install_python_deps = "install_deps")

install_python_deps()

load("@rules_python//python:versions.bzl", get_python_release_url = "get_release_url")

(_, python_url, _) = get_python_release_url("x86_64-unknown-linux-gnu", PYTHON_VERSION)

http_file(
    name = "python3_linux_x86_64_interpreter_archive",
    downloaded_file_path = "python.tar.gz",
    sha256 = "ce1cfca2715e7e646dd618a8cb9baff93000e345ccc979b801fc6ccde7ce97df",
    url = python_url,
)
