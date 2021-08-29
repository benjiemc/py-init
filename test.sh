#!/usr/bin/env bash
set -ex

if [[ -z $VIRTUAL_ENV ]]; then
    virtualenv -p $(which python3) venv
    source venv/bin/activate
fi

pip install -e .[develop]

python setup.py nosetests || error=1

if [[ $error -ne 1 ]]; then
    flake8 pyinit  || true
fi

exit $error

