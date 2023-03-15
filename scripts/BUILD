load("@rules_python//python:defs.bzl", "py_runtime", "py_runtime_pair")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")
load("@io_bazel_rules_docker//container:container.bzl", "container_image", "container_layer")
load("@io_bazel_rules_docker//python:image.bzl", "py_layer")
load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")
load("@python3//:defs.bzl", "host_platform")

exports_files([
    "console_script_template.py",
    "async_console_script_template.py",
])

compile_pip_requirements(
    name = "requirements",
    extra_args = ["--allow-unsafe"],
    requirements_darwin = "requirements_darwin.txt",
    requirements_in = "requirements.in",
    requirements_linux = "requirements_linux.txt",
    tags = ["requires-network"],
    visibility = ["//visibility:public"],
)

py_runtime(
    name = "container_py3_runtime",
    interpreter_path = "/opt/python/bin/python3",
    python_version = "PY3",
    stub_shebang = "#!/opt/python/bin/python3",
)

py_runtime_pair(
    name = "container_py_runtime_pair",
    py3_runtime = ":container_py3_runtime",
)

toolchain(
    name = "container_py_toolchain",
    exec_compatible_with = [
        "@io_bazel_rules_docker//platforms:run_in_container",
    ],
    toolchain = "container_py_runtime_pair",
    toolchain_type = "@rules_python//python:toolchain_type",
)

container_layer(
    name = "python_layer",
    directory = "/opt",
    operating_system = "linux",
    tars = ["@python3_linux_x86_64_interpreter_archive//file"],
    visibility = ["//scripts:__subpackages__"],
)

# container_image(
#     name = "python_base",
#     base = "@rhel8_ubi//image",
#     env = {"SSL_CERT_FILE": "/etc/ssl/certs/ca-bundle.crt"},
#     layers = [":python_layer"],
#     symlinks = {
#         "/usr/bin/python": "/opt/python/bin/python3",
#     },
#     visibility = ["//scripts:__subpackages__"],
# )

# py_layer(
#     name = "pip_tools_deps",
#     deps = [
#         "@pypi__build//:lib",
#         "@pypi__click//:lib",
#         "@pypi__colorama//:lib",
#         "@pypi__importlib_metadata//:lib",
#         "@pypi__pep517//:lib",
#         "@pypi__pip//:lib",
#         "@pypi__pip_tools//:lib",
#         "@pypi__setuptools//:lib",
#         "@pypi__tomli//:lib",
#         "@pypi__wheel//:lib",
#     ],
# )

# py3_image(
#     name = "compile_linux_deps",
#     srcs = [":compile_deps.py"],
#     base = ":python_base",
#     data = [":requirements.in"],
#     layers = [":pip_tools_deps"],
#     main = "compile_deps.py",
#     deps = ["@rules_python//python/runfiles"],
# )

sh_binary(
    name = "compile_all_deps",
    srcs = [":compile_all_deps.sh"],
    data = [
        ":compile_linux_deps",
        ":requirements.update",
    ],
    deps = ["@bazel_tools//tools/bash/runfiles"],
)

# sh_binary(
#     name = "env",
#     srcs = ["env.sh"],
#     args = [
#         "$(PYTHON3)",
#         host_platform,
#     ],
#     data = [
#         "requirements_darwin.txt",
#         "requirements_linux.txt",
#         "@python3",
#         "@python3//:includes",
#     ],
#     toolchains = ["@rules_python//python:current_py_toolchain"],
#     deps = ["@bazel_tools//tools/bash/runfiles"],
# )
