# load("@pypi//:requirements.bzl", "entry_point", dependency = "requirement")
load("@rules_python//python:pip.bzl", "compile_pip_requirements")
load("@rules_python//python:defs.bzl", "py_binary")
load("@pypi//:requirements.bzl", dependency = "requirement")

compile_pip_requirements(
    name = "requirements",
    extra_args = ["--allow-unsafe"],
    # requirements_in = "requirements.in",
    # requirements_linux = "requirements_linux.txt",
    requirements_txt = "requirements.txt",
    tags = ["requires-network"],
    visibility = ["//visibility:public"],
)

py_binary(
    name = "app",
    main = "main.py",
    srcs = ["main.py"],
    # deps = [":utils"],
    deps = [
        dependency("aiohttp"),
        dependency("aiosignal"),
        dependency("async-timeout"),
        dependency("asynctest"),
        dependency("attrs"),
        dependency("certifi"),
        dependency("charset-normalizer"),
        dependency("frozenlist"),
        dependency("idna"),
        dependency("multidict"),
        dependency("openai"),
        dependency("pip"),
        dependency("requests"),
        dependency("setuptools"),
        dependency("tqdm"),
        dependency("typing_extensions"),
        dependency("urllib3"),
        dependency("yarl"),
    ]
)
