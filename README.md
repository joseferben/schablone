# Schablone

Schablone is a highly opinionated Django starter kit based on [cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django). It aims to be a more minimal and lightweight but less configurable alternative.

## Getting started

All you need to generate a project is Python3 and `pip`.

    $ pip install cookiecutter
    $ cookiecutter gh:joseferben/schablone

## Usage

```
Welcome to my_awesome_project
=======================================================

Here are some of the most convenient commands:

- docker              Starts environment with Postgres and Redis using docker-compose, destroys current environment
- data                Runs migrations, creates default user, groups and data
- check               Runs linter and type checker
- fix                 Formats all files and fixes imports
- migrate             Runs migrations
- env                 Starts environment and seeds examples data, destroys current environment!
- test                Runs all tests, requires a database
- shell               Starts an interactive shell with all models imported
- workers             Starts a cluster of worker processes
- run                 Starts the development web server on localhost:8000
- migrations          Creates migrations based on models.py change

Here are some of less used commands:

- graph               Renders a graph with all models in graph.png
- test.coverage       Runs tests and prints coverage
- check.lint          Runs linter
- check.types         Runs type checker
```

## Features

- Heroku-like deployment to [Dokku](https://dokku.com/)
- Local PostgreSQL, Redis and DB UI with [docker-compose](https://docs.docker.com/compose/)
- Static file hosting with [whitenoise](http://whitenoise.evans.io/en/stable/)
- Media file hosting with Dokku [NGINX](https://dokku.com/docs/configuration/nginx/)
- Health checks with [django-health-check](https://django-health-check.readthedocs.io/en/latest/)
- User handling with [django-allauth](https://django-allauth.readthedocs.io/en/latest/overview.html)
- Bootstrap 5 forms with [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- Async and scheduled tasks with [Celery](https://github.com/celery/celery) and [django-celery-beat](https://github.com/celery/django-celery-beat)
- Caching with Redis
- Static types with [pyright](https://github.com/microsoft/pyright)
- Linting with [flake8](https://flake8.pycqa.org/en/latest/)
- Zero-config formatting with [black](https://black.readthedocs.io/en/stable/)
- Free and fast CI pipeline with [CircleCI](https://circleci.com/)

## Design goals

Schablone is heavily inspired by [cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django) but aims to be less configurable. In fact, the project name is pretty much the only thing you can configure. Everything else is trimmed to be suitable for a very specific use case.

### Use case
These are the assumptions of the use case mentioned above.

- Small team
- Minimize hosting cost by self hosting
- Minimize DevOps work (initial and on-going)
- Automated database backups
- Automated zero downtime deployments
- *No* load balancing across machines (one machine only)
- *No* SPA, instead monolith with sprinkled JS

### Differences to cookiecutter-django
Based on the listed assumption, some parts have been replaced by simpler alternatives.

- Replace Heroku, Docker, PythonAnywhere with self-hosted Dokku
- Remove DRF
- Remove Node.js based asset pipeline
- Replace Cloud media file hosting with built-in NGINX of Dokku
- Replace custom CSS build process with vanilla CSS

## Initial setup
These are the steps to set up Dokku.

### Automatic updates
If you use Ubuntu or Debian you can enable automated security updated.

    $ sudo apt install unattended-upgrades
    $ sudo unattended-upgrade

### Dokku

1. Install Dokku according to the [guide](https://dokku.com/docs/getting-started/installation/).
2. Set `alias dokku='ssh -t dokku@<host>` on you machine for better ergonomics
3. Make sure the file `/etc/nginx/sites-available/default` has following content:
```
server {
  listen 80 default_server;
  listen [::]:80 default_server;

  server_name _;
  return 410;
  log_not_found off;
}
```
This makes sure that if the requested host is not valid it will be ignored. By default, Dokku just uses the first app by name which causes a lot of `DisallowedHost` noise if it is a Django app.

Install the redis plugin:

    $ dokku plugin:install https://github.com/dokku/dokku-redis.git redis

### Backups
Create a AWS S3 bucket with a folder `weekly`. Using lifecycle rules it is possible to easily remove backups older than a certain amount of days. You can remove the weekly backups after a year or so.
