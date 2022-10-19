# {{cookiecutter.project_slug}}

Just a simple {{cookiecutter.project_slug}}

## Requirements

* [Memcached](https://memcached.org/)

## Getting started

    $ cp .env.sample .env
    $ pip install -r requirements/local.txt
    $ make docker
    $ make data
    $ make run

A command line tool for TailwindCSS compilation will be downloaded. This might take a few minutes, refresh the browser after that.
## Basic commands

### List all commands

    $ make help

### Create a Superuser

    $ python manage.py createsuperuser
