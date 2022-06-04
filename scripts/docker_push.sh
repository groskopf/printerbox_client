#!/bin/bash
set -x

if [ -z "$CR_PAT" ]; then
  echo "CR_PAT environment variable is not set"
  exit 1;
fi
echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin

image=ghcr.io/groskopf/printerbox_client

docker build -t $image --no-cache . || exit -1
docker push $image:latest
