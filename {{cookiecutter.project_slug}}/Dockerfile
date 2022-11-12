FROM python:3.10.6-slim

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && \
    apt install -y --no-install-recommends build-essential sqlite3 && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ADD https://github.com/benbjohnson/litestream/releases/download/v0.3.9/litestream-v0.3.9-linux-amd64-static.tar.gz /tmp/litestream.tar.gz
RUN tar -C /usr/local/bin -xzf /tmp/litestream.tar.gz && rm /tmp/litestream.tar.gz

RUN mkdir -p /mnt/data && mkdir -p /mnt/cache

WORKDIR /app

COPY requirements/ /app/

RUN pip install -r production.txt


COPY . .


ARG DJANGO_SETTINGS_MODULE="config.settings.production"
ARG DJANGO_SECRET_KEY="for for building purposes"
ARG DJANGO_ADMIN_URL="for for building purposes"
ARG MAILJET_API_KEY="for for building purposes"
ARG MAILJET_SECRET_KEY="for for building purposes"
ARG DB_FILE="for for building purposes"
ARG DB_FILE_QUEUE="for for building purposes"
ARG AWS_ACCESS_KEY_ID="for for building purposes"
ARG AWS_SECRET_ACCESS_KEY="for for building purposes"


RUN python manage.py tailwind installcli
RUN python manage.py tailwind build
RUN python manage.py collectstatic --noinput
RUN python manage.py compress --force


ENTRYPOINT ["/app/scripts/entrypoint.sh"]
