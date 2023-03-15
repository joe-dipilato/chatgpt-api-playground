#!/usr/bin/env bash

if [ $# -eq 0 ]; then
    >&2 echo "No arguments provided"
    exit 1
fi

PACKAGE=$1
VENV_DIR=${2:-/tmp/new_env}

python3 -m venv ${VENV_DIR}
. ${VENV_DIR}/bin/activate
python3 -m pip install ${PACKAGE} 1> /dev/null 2> /dev/null
python3 -m pip list ${PACKAGE} --format freeze 1> ${VENV_DIR}/requirements.txt 2> /dev/null
deactivate

echo
echo "# requirements.txt"
echo
cat ${VENV_DIR}/requirements.txt
echo
echo "# BUILD dependencies"
echo
sed 's/\([^=]*\).*/    dependency("\1"),/' ${VENV_DIR}/requirements.txt
echo

# TODO: optional remove tmp dir