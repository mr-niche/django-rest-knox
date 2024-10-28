FROM python:3.12-slim-bullseye

RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

RUN pip install tox

WORKDIR /app