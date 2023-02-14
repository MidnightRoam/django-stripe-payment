FROM python:3.9-alpine3.16

COPY requirements.txt /temp/requirements.txt
RUN apk add --no-cache sqlite
RUN pip install -r /temp/requirements.txt
COPY service /service
WORKDIR /service
EXPOSE 8000

RUN adduser --disabled-password service-user

USER service-user