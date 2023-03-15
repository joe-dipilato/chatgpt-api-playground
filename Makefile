default: run
build:
	bazel sync --only pypi
	bazel build app
run:
	bazel run app
clean:
	bazel clean
watch:
	./watch.sh main.py "$(MAKE) run"