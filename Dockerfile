FROM balenalib/raspberry-pi-debian-python:latest


COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

RUN mkdir /app
COPY *.py /app/
COPY fast-api-client/*.py /app/
RUN pip install --no-cache-dir --upgrade /app/fast-api-client
