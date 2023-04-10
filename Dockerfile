FROM python:3.9-slim-buster

WORKDIR /usr/src/app

ADD requirements.txt ./requirements.txt

RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && apt-get purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install -U pip && pip install -r requirements.txt 
RUN pip install git+https://github.com/maistodos/python-creditcard.git@main

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["sh", "docker-entrypoint.sh"]