FROM printerbox_python:v2

RUN mkdir -p /app/src/fast-api-client
COPY fast-api-client/ /app/src/fast-api-client
RUN pip install --no-cache-dir --upgrade /app/src/fast-api-client

RUN mkdir -p /app/src
COPY src/*.py /app/src/

