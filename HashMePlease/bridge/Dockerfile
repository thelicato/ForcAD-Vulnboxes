FROM python:3.11.6-slim-bullseye

WORKDIR /app
COPY . ./
RUN pip install . && rm -rf ./**

ENTRYPOINT ["hashmeplease_bridge"]