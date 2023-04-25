# {{cookiecutter.project_slug}}

Just a simple {{cookiecutter.project_slug}}

## Running locally

    $ python -m venv .venv
    $ source .venv/bin/activate
    $ pip install -r requirements/dev.txt
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
