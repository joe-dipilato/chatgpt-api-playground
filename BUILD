# load("@pypi//:requirements.bzl", "entry_point", dependency = "requirement")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")

compile_pip_requirements(
    name = "requirements",
    extra_args = ["--allow-unsafe"],
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

py_binary(
    name = "app",
    main = "main.py",
    srcs = ["main.py"],
    # deps = [":utils"],
)
