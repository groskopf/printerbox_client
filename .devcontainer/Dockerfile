FROM python:3.10

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

#RUN apt update && apt install -y \
#    npm \
#    && rm -rf /var/lib/{apt,dpkg,cache,log}/
#RUN npm install @openapitools/openapi-generator-cli -g

#Autogen is not currently working
#RUN pip install openapi-python-client

#RUN openapi-python-client generate --url http://127.0.0.1:8000/openapi.json && \
#COPY openapi.json /app/openapi.json
RUN openapi-python-client generate --path openapi.json && \
    pip install --no-cache-dir fast-api-client


RUN   pip install --no-cache-dir ./fast-api-client


CMD ["python", "main:app"]
