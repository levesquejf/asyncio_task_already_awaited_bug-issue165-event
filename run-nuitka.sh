#!/usr/bin/env bash

set -euxo pipefail

docker build -t asyncio-bug-nuitka -f Dockerfile-nuitka .
docker run asyncio-bug-nuitka
