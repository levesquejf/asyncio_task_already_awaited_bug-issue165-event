#!/usr/bin/env bash

set -euxo pipefail

docker build -t asyncio-bug-native -f Dockerfile-native .
docker run asyncio-bug-native
