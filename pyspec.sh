#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)"
SPEC_DIRECTORY="tests"

if ! command -v python &>/dev/null; then
  echo "python command not found, please ensure python is installed and in your PATH." 1>&2
  exit 1
fi

if [ ! -d "${SPEC_DIRECTORY}" ]; then
  echo "No test directory found locally, please ensure that there is a tests/ directory readable by this user"
  exit 1
fi

if [ -n $1 ]; then
  python -m unittest $1
else
  python -m unittest discover $SPEC_DIRECTORY
fi
