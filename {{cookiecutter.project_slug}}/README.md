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

1. `dokku apps:create {{cookiecutter.project_slug}}`
2. `dokku domains:add {{cookiecutter.project_slug}} {{cookiecutter.domain}} www.{{cookiecutter.domain_name}}`
3. `dokku postgres:create {{cookiecutter.project_slug}}database`
4. `dokku postgres:link {{cookiecutter.project_slug}}database {{cookiecutter.project_slug}}`
5. `dokku redis:create {{cookiecutter.project_slug}}redis`
6. `dokku postgres:link {{cookiecutter.project_slug}}redis {{cookiecutter.project_slug}}`
7. `dokku config:set --no-restart {{cookiecutter.project_slug}} DJANGO_SETTINGS_MODULE=config.settings.production EMAIL_HOST= EMAIL_HOST_USER= EMAIL_HOST_PASSWORD= SECRET_KEY= SENTRY_DSN= DOKKU_LETSENCRYPT_EMAIL=`
8. `git remote add dokku dokku@<host>:{{cookiecutter.project_slug}}`
9. `git push dokku master:master`
10. `dokku letsencrypt:enable {{cookiecutter.project_slug}}`
11. `dokku run movinmalta "python loaddata homes/fixtures/default/*`
12. Change the admin password `admin:password`
13. `dokku postgres:backup-auth {{cookiecutter.project_slug}}database <aws-access-key-id> <aws-secret-access-key>`
14. `dokku postgres:backup-set-encryption {{cookiecutter.project_slug}}database <encryption-key>`
15. `dokku postgres:backup {{cookiecutter.project_slug}}database <s3-bucket>` and verify that the backup worked
16. `dokku postgres:backup-schedule {{cookiecutter.project_slug}}database @daily <s3-bucket>`


### Configuration
1. Configure Email [django docs]()
2. Configure Sentry (SENTRY_KEY, SENTRY_HOST, SENTRY_PATH)
3. Configure database (DATBASE_URL)
4. Configure Redis (REDIS_URL)
5. Configure Google Analytics (GOOGLE_ANALYTICS_KEY)

### Deployment
