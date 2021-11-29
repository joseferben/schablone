# Schablone

This is a highly opinionated Django starter kit based on [cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django).

## Getting started
1. `mkdir pizza_shop`
2. `cd pizza_shop`
3. `python3 -m venv .venv`
4. `source pizza_shop/bin/activate`

## Features

The driving goal of Schablone is simplicity.

- Optimized for deployment on Dokku
- Docker Compose for local development
- Static file hosting with whitenoise
- Media file hosting with NGINX
- Health checks
- User handling with django-allauth
- Crispy forms with Bootstrap 5 support
- Django Q for async tasks and cron jobs using Redis as broker
- Caching with Redis
- Monitoring with Sentry
- HTMX for dynamic elements
- Google Analytics for analytics
- Static types with mypy
- Linting with flake8
- CircleCI CI pipeline

## Configuration
1. Configure Email [django docs]()
2. Configure Sentry (SENTRY_KEY, SENTRY_HOST, SENTRY_PATH)
3. Configure database (DATBASE_URL)
4. Configure Redis (REDIS_URL)
5. Configure Google Analytics (GOOGLE_ANALYTICS_KEY)

## Deployment
1. todo
2. todo
