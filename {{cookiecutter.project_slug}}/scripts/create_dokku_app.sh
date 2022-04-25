#!/bin/sh

DOKKU_HOST="${DOKKU_HOST:-lettuce}"
AWS_S3_BACKUP_PATH="${AWS_S3_BACKUP_PATH:-lettuce-backups/daily}"

echo "create app"
ssh -t dokku@${DOKKU_HOST} apps:create {{cookiecutter.project_slug}}
ssh -t dokku@${DOKKU_HOST} domains:add {{cookiecutter.project_slug}} {{cookiecutter.domain_name}}

echo "set up database"
ssh -t dokku@${DOKKU_HOST} postgres:create {{cookiecutter.project_slug}}-database
ssh -t dokku@${DOKKU_HOST} postgres:link {{cookiecutter.project_slug}}-database {{cookiecutter.project_slug}}

echo "set up redis"
ssh -t dokku@${DOKKU_HOST} redis:create {{cookiecutter.project_slug}}-redis
ssh -t dokku@${DOKKU_HOST} redis:link {{cookiecutter.project_slug}}-redis {{cookiecutter.project_slug}}

echo "configure app"
ssh -t dokku@${DOKKU_HOST} config:set --no-restart {{cookiecutter.project_slug}} DJANGO_DEBUG=False
ssh -t dokku@${DOKKU_HOST} config:set --no-restart {{cookiecutter.project_slug}} DJANGO_SETTINGS_MODULE=config.settings.production
ssh -t dokku@${DOKKU_HOST} config:set --no-restart {{cookiecutter.project_slug}} DJANGO_SECRET_KEY="$(openssl rand -base64 64 | tr -dc 'A-HJ-NP-Za-km-z2-9' | head -c 64)"
ssh -t dokku@${DOKKU_HOST} config:set --no-restart {{cookiecutter.project_slug}} DJANGO_ADMIN_URL="$(openssl rand -base64 4096 | tr -dc 'A-HJ-NP-Za-km-z2-9' | head -c 32)/"
ssh -t dokku@${DOKKU_HOST} config:set --no-restart {{cookiecutter.project_slug}} MAILJET_API_KEY=${MAILJET_API_KEY}
ssh -t dokku@${DOKKU_HOST} config:set --no-restart {{cookiecutter.project_slug}} MAILJET_SECRET_KEY=${MAILJET_SECRET_KEY}

echo "mount media files to docker volume"
ssh root@${DOKKU_HOST} -f 'mkdir -p /var/lib/dokku/data/storage/{{cookiecutter.project_slug}}/'
ssh root@${DOKKU_HOST} -f 'chown -R dokku:dokku /var/lib/dokku/data/storage/{{cookiecutter.project_slug}}/'
ssh -t dokku@${DOKKU_HOST} storage:mount {{cookiecutter.project_slug}} /var/lib/dokku/data/storage/{{cookiecutter.project_slug}}:/storage

echo "serve media files using nginx"
ssh root@${DOKKU_HOST} -f 'mkdir -p /home/dokku/{{cookiecutter.project_slug}}/nginx.conf.d'
ssh root@${DOKKU_HOST} -f 'echo "location /media {" > /home/dokku/{{cookiecutter.project_slug}}/nginx.conf.d/media.conf'
ssh root@${DOKKU_HOST} -f 'echo "    alias /var/lib/dokku/data/storage/{{cookiecutter.project_slug}};" >> /home/dokku/{{cookiecutter.project_slug}}/nginx.conf.d/media.conf'
ssh root@${DOKKU_HOST} -f 'echo "}" >> /home/dokku/{{cookiecutter.project_slug}}/nginx.conf.d/media.conf'
ssh root@${DOKKU_HOST} -f 'chown -R dokku:dokku /home/dokku/{{cookiecutter.project_slug}}/nginx.conf.d'

echo "set up daily backups to s3"
ssh -t dokku@${DOKKU_HOST} postgres:backup-set-encryption {{cookiecutter.project_slug}}-database ${BACKUP_ENCRYPTION_KEY}
ssh -t dokku@${DOKKU_HOST} postgres:backup-auth {{cookiecutter.project_slug}}-database ${AWS_ACCESS_KEY_ID} ${AWS_SECRET_ACCESS_KEY}
ssh -t dokku@${DOKKU_HOST} postgres:backup-schedule {{cookiecutter.project_slug}}-database @daily ${AWS_S3_BACKUP_PATH}

echo "test backup to s3"
ssh -t dokku@${DOKKU_HOST} postgres:backup {{cookiecutter.project_slug}}-database ${AWS_S3_BACKUP_PATH}

echo "add dokku host as git remote"
git remote add dokku dokku@${DOKKU_HOST}:{{cookiecutter.project_slug}}
