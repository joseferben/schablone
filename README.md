# schablone

schablone is a highly opinionated Django starter kit based on [cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django). It aims to be a more minimal and lightweight but less configurable alternative.

## Getting started

All you need to generate a project is Python3 and `pip`.

    $ pip install cookiecutter
    $ cookiecutter gh:joseferben/schablone

## Usage

`$ make`

```
Welcome to website
=======================================================

Here are some of the most convenient commands:

- dev                 Starts the development web server on localhost:8000
- check               Lints and fixes codebase
- work                Run huey worker process
- migrate             Applies pending migrations
- test                Runs all tests
- shell               Starts an interactive shell with all models imported
- migrations          Creates migrations based on models.py change
- webp                Compresses static images to webp (requires imagemagick)

Here are some of less used commands:

- coverage            Runs tests and prints coverage in terminal
- check.lint          Runs linter
- check.types         Runs type checker
- watch.server        Runs web server on localhost:8000
```

## Features & Design goals

- Styling of semantic HTML with [PicoCSS](https://picocss.com/)
- Production data persisted using [SQLite](https://www.sqlite.org/index.html)
- Database backups using [Litestream](https://litestream.io/)
- Health checks with [django-health-check](https://django-health-check.readthedocs.io/en/latest/)
- Magic-link login using [django-sesame](https://github.com/aaugustin/django-sesame)
- Mail sending using [Anymail](https://anymail.dev/en/stable/)
- Async and scheduled tasks with [huey](https://github.com/coleifer/huey)
- Zero-config formatting, linting and auto-fixing with [black](https://black.readthedocs.io/en/stable/) and [flake8](https://flake8.pycqa.org/en/latest/)
- Static typing with [pyright](https://github.com/microsoft/pyright)
- Simple test assertions using [pytest](https://github.com/pytest-dev/pytest)
- Ready to be deployed to Heroku or [Dokku](https://dokku.com/)

Read about the [design decisions](https://www.joseferben.com/posts/schablone-django-starter-template-for-simplicity/) in my blog at [joseferben.com](http://www.joseferben.com).

## Dokku config

Example config:

```
AWS_ACCESS_KEY_ID:       <hidden>
AWS_SECRET_ACCESS_KEY:   <hidden>
DB_FILE:                 /databases/db.sqlite3
DB_FILE_QUEUE:           /databases/huey.sqlite3
DISABLE_COLLECTSTATIC:   1
DJANGO_ADMIN_URL:        <hidden>
DJANGO_SECRET_KEY:       <hidden>
DJANGO_SETTINGS_MODULE:  config.settings.production
POSTMARK_SERVER_TOKEN:   <hidden>
SENTRY_DSN:              <hidden>
```
