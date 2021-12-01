# {{cookiecutter.project_name}}

This Django project was generated with [schablone](https://github.com/joseferben/schablone).

## Local development

### Prerequisites
In order to develop locally you need following packages.

- make
- bash
- Python 3
- Docker
- docker-compose

### Commands
1. `make init`
2. `source .venv/bin/activate`
3. `make docker`
4. `make data`
5. `make workers`
6. `make run`

or run `make` to get a list of all possible commands.

## Architecture and design
TODO

## Running in production

### Dokku setup

### Configuration
1. Configure Email [django docs]()
2. Configure Sentry (SENTRY_KEY, SENTRY_HOST, SENTRY_PATH)
3. Configure database (DATBASE_URL)
4. Configure Redis (REDIS_URL)
5. Configure Google Analytics (GOOGLE_ANALYTICS_KEY)

### Deployment
