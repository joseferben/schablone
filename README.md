# schablone

schablone is a highly opinionated Django starter kit based on [cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django). It aims to be a more minimal and lightweight but less configurable alternative.

## Getting started

All you need to generate a project is Python3 and `pip`.

    $ pip install cookiecutter
    $ cookiecutter gh:joseferben/schablone

## Usage

`$ make`

```
Welcome to my_awesome_project
=======================================================

Here are some of the most convenient commands:

- data                Runs migrations, creates default user, groups and data
- dev                 Starts the development web server on localhost:8000
- work                Runs a huey worker process
- check               Runs linter and type checker
- migrations          Creates migrations based on models.py change
- migrate             Runs migrations
- test                Runs all tests, requires a database
- shell               Starts an interactive shell with all models imported
- webp                Compresses static images to webp

Here are some of less used commands:

- graph               Renders a graph with all models in graph.png
- test.coverage       Runs tests and prints coverage
- check.lint          Runs linter
- check.types         Runs type checker
- watch.server        Runs web server on localhost:8000
- watch.css           Runs the TailwindCSS compiler
```

## Features & Design goals

- Deployment to [fly.io](https://fly.io/)
- Production data persisted using [SQLite](https://www.sqlite.org/index.html)
- Database backups using [Litestream](https://litestream.io/)
- Health checks with [django-health-check](https://django-health-check.readthedocs.io/en/latest/)
- Magic-link login using [django-sesame](https://github.com/aaugustin/django-sesame)
- TailwindCSS without Node.js using [django-tailwind-cli](https://github.com/oliverandrich/django-tailwind-cli)
- [Custom form rendering](https://www.joseferben.com/posts/django-4-form-tailwind-without-node-crispy/) without dependencies such as django-crispy-forms
- Mail sending using [Anymail](https://anymail.dev/en/stable/)
- Async and scheduled tasks with [huey](https://github.com/coleifer/huey)
- Zero-config formatting, linting and auto-fixing with [black](https://black.readthedocs.io/en/stable/) and [flake8](https://flake8.pycqa.org/en/latest/)
- Static typing with [pyright](https://github.com/microsoft/pyright)
- Simple test assertions using [pytest](https://github.com/pytest-dev/pytest)

Read about the [design decisions](https://www.joseferben.com/posts/schablone-django-starter-template-for-simplicity/) in my blog at [joseferben.com](http://www.joseferben.com).
