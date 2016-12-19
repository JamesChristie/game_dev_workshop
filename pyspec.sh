#!/usr/bin/env bash

SPEC_DIRECTORY="tests"
PYTHON="python3"

if ! command -v $PYTHON &>/dev/null; then
  echo "The '${PYTHON}' command not found, please ensure Python 3 is installed and in your PATH." 1>&2
  exit 1
fi

if [ ! -d "${SPEC_DIRECTORY}" ]; then
  echo "No test directory found locally, please ensure that there is a tests/ directory readable by this user"
  exit 1
fi

if [ -n $1 ]; then
  $PYTHON -m unittest $1
else
  $PYTHON -m unittest discover $SPEC_DIRECTORY
fi
