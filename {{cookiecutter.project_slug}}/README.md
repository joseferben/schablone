# {{cookiecutter.project_slug}}

Just a simple {{cookiecutter.project_slug}}

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Getting started

    $ cp .env.sample .env
    $ pip install -r requirements/local.txt
    $ make docker

## Basic commands

### List all commands

    $ make help

### Create a Superuser

    $ python manage.py createsuperuser

## Deployment

Adjust the script `create_dokku_app.sh` if needed.

    $ export AWS_S3_BACKUP_PATH=lettuce-backups/daily
    $ export DOKKU_HOST=lettuce
    $ export AWS_ACCESS_KEY_ID=<key>
    $ export AWS_SECRET_ACCESS_KEY=<secret>
    $ export BACKUP_ENCRYPTION_KEY=<key>
    $ export MAILJET_API_KEY=<key>
    $ export MAILJET_SECRET_KEY=<secret>
    $ ./scripts/create_dokku_app.sh
    $ git push dokku main

### Let's Encrypt

Make sure to disable any proxies such a Cloudflare so Let's Encrypt can do it's work.

    $ sudo dokku plugin:install https://github.com/dokku/dokku-letsencrypt.git
    $ dokku letsencrypt:enable {{cookiecutter.project_slug}}
