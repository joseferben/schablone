#!/bin/sh

set -e

DOKKU_HOST="${DOKKU_HOST:-lettuce}"
AWS_S3_BACKUP_PATH="${DOKKU_HOST:-lettuce-backups/daily}"

# install redis plugin
ssh -t dokku@lettuce plugin:install https://github.com/dokku/dokku-redis.git redis

# create app
ssh -t dokku@lettuce apps:create {{cookiecutter.project_slug}}
ssh -t dokku@lettuce domains:add {{cookiecutter.project_slug}} {{cookiecutter.domain_name}}

# set up database
ssh -t dokku@lettuce postgres:create {{cookiecutter.project_slug}}-database
ssh -t dokku@lettuce postgres:link {{cookiecutter.project_slug}}-database {{cookiecutter.project_slug}}

# set up redis
ssh -t dokku@lettuce redis:create {{cookiecutter.project_slug}}-redis
ssh -t dokku@lettuce redis:link {{cookiecutter.project_slug}}-redis {{cookiecutter.project_slug}}

# set up configuration
ssh -t dokku@lettuce config:set --no-restart {{cookiecutter.project_slug}} DJANGO_DEBUG=False
ssh -t dokku@lettuce config:set --no-restart {{cookiecutter.project_slug}} DJANGO_SETTINGS_MODULE=config.settings.production
ssh -t dokku@lettuce config:set --no-restart {{cookiecutter.project_slug}} DJANGO_SECRET_KEY="$(openssl rand -base64 64)"
ssh -t dokku@lettuce config:set --no-restart {{cookiecutter.project_slug}} DJANGO_ADMIN_URL="$(openssl rand -base64 4096 | tr -dc 'A-HJ-NP-Za-km-z2-9' | head -c 32)/"
ssh -t dokku@lettuce config:set --no-restart {{cookiecutter.project_slug}} MAILJET_API_KEY=${MAILJET_API_KEY}
ssh -t dokku@lettuce config:set --no-restart {{cookiecutter.project_slug}} MAILJET_SECRET_KEY=${MAILJET_SECRET_KEY}

# set up media file serving
ssh root@lettuce -f 'mkdir -p /var/lib/dokku/data/storage/{{cookiecutter.project_slug}}/'
ssh root@lettuce -f 'chown -R dokku:dokku /var/lib/dokku/data/storage/{{cookiecutter.project_slug}}/'
ssh -t dokku@lettuce storage:mount {{cookiecutter.project_slug}} /var/lib/dokku/data/storage/{{cookiecutter.project_slug}}:/storage
ssh root@lettuce -f 'mkdir -p /home/dokku/{{cookiecutter.project_slug}}/nginx.conf.d'
ssh root@lettuce -f 'echo "location /media {" >> /home/dokku/{{cookiecutter.project_slug}}/nginx.conf.d/media.conf'
ssh root@lettuce -f 'echo "    alias /var/lib/dokku/data/storage/{{cookiecutter.project_slug}};" >> /home/dokku/{{cookiecutter.project_slug}}/nginx.conf.d/media.conf'
ssh root@lettuce -f 'echo "}" >> /home/dokku/{{cookiecutter.project_slug}}/nginx.conf.d/media.conf'
ssh root@lettuce -f 'chown -R dokku:dokku /home/dokku/{{cookiecutter.project_slug}}/nginx.conf.d/media.conf'

# set up daily database backups to s3
ssh -t dokku@lettuce postgres:backup-set-encryption {{cookiecutter.project_slug}}-database ${BACKUP_ENCRYPTION_KEY}
ssh -t dokku@lettuce postgres:backup-auth {{cookiecutter.project_slug}}-database ${AWS_ACCESS_KEY_ID} ${AWS_SECRET_ACCESS_KEY}
ssh -t dokku@lettuce postgres:backup-schedule {{cookiecutter.project_slug}}-database @daily ${AWS_S3_BACKUP_PATH}

# add dokku host as git remote
git remote add dokku dokku@${DOKKU_HOST}:{{cookiecutter.project_slug}}
