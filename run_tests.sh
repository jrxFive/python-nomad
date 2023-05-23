#!/bin/bash
#
# Run tests with local Nomad binaries. 
set -ueo pipefail

if [ "${1-}" == "init" ]; then
    virtualenv .venv
    pip install -r requirements-dev.txt
    source .venv/bin/activate
fi

NOMAD_VERSION=`nomad --version | awk '{print $2}' | cut -c2-` 

echo "Run Nomad in dev mode"
nomad agent -dev -node pynomad1 --acl-enabled &> nomad.log &
NOMAD_PID=$!

sleep 3

echo "Run tests with Nomad $NOMAD_VERSION"
NOMAD_IP=127.0.0.1 NOMAD_VERSION=$NOMAD_VERSION py.test -s --cov=nomad --cov-report=term-missing --runxfail tests/ || true


echo "Kill nomad in background"
kill ${NOMAD_PID}
