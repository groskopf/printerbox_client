#!/bin/bash
set -x

if [ -z "$CR_PAT" ]; then
  echo "CR_PAT environment variable is not set"
  exit 1;
fi
echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin

image=ghcr.io/groskopf/printerbox_client_dev

docker build -t $image Dockerfile.dev
docker push $image:latest
