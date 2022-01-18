FROM python:2

ENV PYTHONUNBUFFERED 1
RUN apt update && apt remove -yqq python3 --autoremove
RUN pip install --upgrade pip
RUN mkdir /var/app
WORKDIR /var/app
COPY src/deploy/requirements.txt src/deploy/requirements.txt
RUN pip install -r src/deploy/requirements.txt
COPY . .
