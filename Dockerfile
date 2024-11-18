FROM python:3.12.2-slim-bullseye

RUN apt-get update \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/app
COPY ./requirements.txt /opt/app

RUN pip install python-dateutil
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8080
CMD ["flask","run"]