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

## Deployment

### Create services
Create a {{cookiecutter.project_slug}} app, a PostgreSQL instance and a Redis instance.
1. `dokku apps:create {{cookiecutter.project_slug}}`
2. `dokku domains:add {{cookiecutter.project_slug}} {{cookiecutter.domain_name}} www.{{cookiecutter.domain_name}}`
3. `dokku postgres:create {{cookiecutter.project_slug}}-database`
4. `dokku postgres:link {{cookiecutter.project_slug}}-database {{cookiecutter.project_slug}}`
5. `dokku redis:create {{cookiecutter.project_slug}}-redis`
6. `dokku redis:link {{cookiecutter.project_slug}}-redis {{cookiecutter.project_slug}}`

### Configuration
```sh
dokku config:set --no-restart {{cookiecutter.project_slug}} \
  DJANGO_SETTINGS_MODULE=config.settings.production \
  EMAIL_HOST= EMAIL_HOST_USER= \
  EMAIL_HOST_PASSWORD= SECRET_KEY= \
  SENTRY_DSN= \
  DOKKU_LETSENCRYPT_EMAIL= \
  GOOGLE_ANALYTICS_KEY=
```

### Set secret key
1. `dokku config:set --no-restart {{cookiecutter.project_slug}} \
  SECRET_KEY=$(python manage.py generate_secret_key)`

### Serving media files using NGINX
We are using whitenoise + CDN to host static files. They don't change frequently and can be cached easily. Media files, which are uploaded by users, are served by the NGINX instance that Dokku is using.
Based on this blog post: https://codelv.com/blog/2018/10/serving-static-and-media-files-with-dokku

1. `mkdir /var/lib/dokku/data/storage/{{cookiecutter.project_slug}}/`
2. `chown -R dokku:dokku /var/lib/dokku/data/storage/{{cookiecutter.project_slug}}/`
3. `dokku storage:mount {{cookiecutter.project_slug}} /var/lib/dokku/data/storage/{{cookiecutter.project_slug}}:/storage`
4. `mkdir -p /home/dokku/{{cookiecutter.project_slug}}/nginx.conf.d`
5. `vim /home/dokku/{{cookiecutter.project_slug}}/nginx.conf.d/media.conf`
With following content:
```nginx
location /media {
    alias /var/lib/dokku/data/storage/{{cookiecutter.project_slug}};
}
```
6. `chown -R dokku:dokku /home/dokku/{{cookiecutter.project_slug}}/nginx.conf.d/media.conf`
7. `dokku ps:restart {{cookiecutter.project_slug}}`

### Set up rate limiting (optional)
If you need rate limiting, use NGINX to do that efficiently. Don't forget to use `$http_cf_connecting_ip` if using Cloudflare.

```
limit_req_zone $http_cf_connecting_ip zone=ip:10m rate=5r/s;
limit_req zone=ip burst=5 nodelay;

limit_conn_status 429;
limit_req_status 429;
```

### Initial deployment
1. `git remote add dokku dokku@<host>:{{cookiecutter.project_slug}}`
2. `git push dokku master:master`

### Enable TLS
1. `dokku letsencrypt:enable {{cookiecutter.project_slug}}`

### Creating initial admin
1. `dokku run {{cookiecutter.project_slug}} "python manage.py loaddata {{cookiecutter.project_slug}}/fixtures/default/*"`
2. Change the admin password `admin:password`

### Scheduling database backups
Create an S3 bucket on AWS for automated periodic backups.

1. `dokku postgres:backup-auth {{cookiecutter.project_slug}}-database <aws-access-key-id> <aws-secret-access-key>`
2. `dokku postgres:backup-set-encryption {{cookiecutter.project_slug}}-database <encryption-key>`
3. `dokku postgres:backup {{cookiecutter.project_slug}}-database <s3-bucket>` and verify that the backup worked
4. `dokku postgres:backup-schedule {{cookiecutter.project_slug}}-database @weekly <s3-bucket>/weekly`

### Next steps
- Setup a CDN like Cloudflare because of whitenoise
- Setup uptimerobot.com for https://{{cookiecutter.domain_name}}/ht
