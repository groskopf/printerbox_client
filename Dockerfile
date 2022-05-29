FROM balenalib/raspberry-pi-debian-python:latest

ENV UDEV=1

VOLUME /data
WORKDIR /data

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

RUN apt-get update && apt-get install -y \
    dnsutils \
    cups-bsd \
    cups-client \
    npm \
    && apt-get clean \
    && rm -rf /var/lib/{apt,dpkg,cache,log}/

RUN npm install @openapitools/openapi-generator-cli -g

RUN openapi-python-client generate --url https://api.printerboks.dk/api/v1/openapi.json && \
    pip install --no-cache-dir fast-api-client

COPY blink/blink1-tool /usr/bin
COPY blink/51-blink1.rules /etc/udev/rules.d/51-blink1.rules

