FROM python:3.7

ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -yqq python3-psycopg2
RUN pip install --upgrade pip
RUN mkdir /var/app
WORKDIR /var/app
COPY src/deploy/requirements.txt src/deploy/requirements.txt
RUN pip install -r src/deploy/requirements.txt
COPY . .
