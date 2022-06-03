FROM printerbox_python:v2


#COPY requirements.txt /tmp/requirements.txt
#RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

RUN mkdir -p /app/src
COPY *.py /app/src/

RUN mkdir -p /app/src/fast-api-client
COPY fast-api-client/ /app/src/fast-api-client
RUN pip install --no-cache-dir --upgrade /app/src/fast-api-client
