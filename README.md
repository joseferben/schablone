# Schablone

Schablone is a highly opinionated Django starter kit based on [cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django). It aims to be a more minimal and lightweight but less configurable alternative.

## Getting started

All you need to generate a project is Python 3 and `pip`.

1. `pip install cookiecutter`
2. `cookiecutter gh:joseferben/schablone`
3. `Answer the wizard`
4. `cp .env.sample .env`

## Usage

Refer to the README.md of the generated project.

## Features

- Heroku-like deployment to [Dokku](https://dokku.com/)
- Local PostgreSQL, Redis and DB UI with [docker-compose](https://docs.docker.com/compose/)
- Static file hosting with [whitenoise](http://whitenoise.evans.io/en/stable/)
- Media file hosting with Dokku [NGINX](https://dokku.com/docs/configuration/nginx/)
- Health checks with [django-health-check](https://django-health-check.readthedocs.io/en/latest/)
- User handling with [django-allauth](https://django-allauth.readthedocs.io/en/latest/overview.html)
- Bootstrap 5 forms with [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- Async and scheduled tasks with [django-q](https://django-q.readthedocs.io/en/latest/)
- Caching with Redis
- Monitoring with [Sentry](https://sentry.io/)
- Dynamic elements with [HTMX](https://htmx.org/)
- Analytics with Google Analytics
- Static types with [mypy](http://mypy-lang.org/)
- Linting with [flake8](https://flake8.pycqa.org/en/latest/)
- Zero-config formatting with [black](https://black.readthedocs.io/en/stable/)
- Free and fast CI pipeline with [CircleCI](https://circleci.com/)

## Design goals

Schablone is heavily inspired by [cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django). The project layout, templates, Bootstrap 5 forms and configuration handling are the same. However, Schablone aims to be more minimal.

The template itself does not have that many configuration options, which makes it easier to maintain.

The components and dependencies have been picked to be "good enough" for a specific use case.

### Assumptions
These are the assumptions of that use case.

- Small team
- Minimize hosting cost by self hosting
- Minimize DevOps work (initial and operational)
- Automated database backups
- Automated zero downtime deployments
- *No* load balancing across machines (one machine only)
- *No* SPA, instead monolith with sprinkled JS

### Differences to cookiecutter-django
Based on the listed assumption, some parts have been replaced by simpler alternatives.

- Replace Heroku, Docker, PythonAnywhere with self-hosted Dokku
- Replace DRF with HTMX and custom JS
- Replace Celery with Django Q as lightweight (and less capable) alternative
- Replace Cloud media file hosting with built-in NGINX of Dokku
- Replace custom CSS build process with vanilla CSS

## Initial setup
These steps need to be taken initially after provisioning the machine.

### Automatic updates
If you use Ubuntu or Debian you can enable automated security updated.

```sh
sudo apt install unattended-upgrades
sudo unattended-upgrade
```

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

### Backups
Create a AWS S3 bucket with a folder `weekly`. Using lifecycle rules it is possible to easily remove backups older than a certain amount of days. You can remove the weekly backups after a year or so.
