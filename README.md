# Project

Just a simple schablone project

## Running locally

Replace all `project.com` references with your own domain, check TODOs in the code for renaming.

    $ python -m venv .venv
    $ source .venv/bin/activate
    $ pip install -r requirements/dev.txt
    $ ./manage.py tailwind installcli
    $ ./manage.py tailwind build
    $ make dev

## Config

```
AWS_ACCESS_KEY_ID:       <hidden>
AWS_SECRET_ACCESS_KEY:   <hidden>
DISABLE_COLLECTSTATIC:   1
DJANGO_SECRET_KEY:       <hidden>
DJANGO_SETTINGS_MODULE:  config.settings.production
POSTMARK_SERVER_TOKEN:   <hidden>
SENTRY_DSN:              <hidden>
```
