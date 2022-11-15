#!/bin/bash
#
# Run tests with local Nomad binaries. 
set -ueo pipefail

if [ "${1-}" == "init" ]; then
    virtualenv .venv
    pip install -r requirements-dev.txt
fi

source .venv/bin/activate
NOMAD_VERSION=`nomad --version | awk '{print $2}' | cut -c2-` 

echo "Run tests with Nomad $NOMAD_VERSION"
NOMAD_IP=127.0.0.1 NOMAD_VERSION=$NOMAD_VERSION py.test -s --cov=nomad --cov-report=term-missing --runxfail tests/