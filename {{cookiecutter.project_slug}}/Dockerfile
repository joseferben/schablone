FROM python:3.10.6

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && \
    apt install -y \
    gettext \
    zlib1g-dev \
    libpq-dev \
    libtiff5-dev \
    libjpeg62-turbo-dev \
    libfreetype6-dev \
    liblcms2-dev \
    memcached \
    libwebp-dev && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements/ /app/

RUN pip install -r production.txt

COPY . .

ARG DJANGO_SETTINGS_MODULE="config.settings.production"
ARG DJANGO_SECRET_KEY="for for building purposes"
ARG REDIS_URL="for for building purposes"
ARG DATABASE_URL="for for building purposes"
ARG DJANGO_ADMIN_URL="for for building purposes"
ARG MAILJET_API_KEY="for for building purposes"
ARG MAILJET_SECRET_KEY="for for building purposes"

RUN tailwindcss --minify -i {{cookiecutter.project_slug}}/static/css/project.css -o {{cookiecutter.project_slug}}/static/css/dist/styles.css
RUN python manage.py compress
RUN python manage.py collectstatic --noinput

CMD gunicorn config.wsgi:application
