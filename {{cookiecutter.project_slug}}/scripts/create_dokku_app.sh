#!/bin/sh

# TODO MAILJET_API_KEY
# TODO MAILJET_SECRET_KEY

ssh -t dokku@lettuce apps:create {{cookiecutter.project_slug}}
ssh -t dokku@lettuce domains:add {{cookiecutter.project_slug}} {{cookiecutter.domain_name}}
ssh -t dokku@lettuce postgres:create {{cookiecutter.project_slug}}-database
ssh -t dokku@lettuce postgres:link {{cookiecutter.project_slug}}-database {{cookiecutter.project_slug}}
ssh -t dokku@lettuce redis:create {{cookiecutter.project_slug}}-redis
ssh -t dokku@lettuce redis:link {{cookiecutter.project_slug}}-redis {{cookiecutter.project_slug}}
ssh -t dokku@lettuce config:set --no-restart {{cookiecutter.project_slug}} DJANGO_DEBUG=False
ssh -t dokku@lettuce config:set --no-restart {{cookiecutter.project_slug}} DJANGO_SETTINGS_MODULE=config.settings.production
ssh -t dokku@lettuce config:set --no-restart {{cookiecutter.project_slug}} DJANGO_SECRET_KEY="$(openssl rand -base64 64)"
ssh -t dokku@lettuce config:set --no-restart {{cookiecutter.project_slug}} DJANGO_ADMIN_URL="$(openssl rand -base64 4096 | tr -dc 'A-HJ-NP-Za-km-z2-9' | head -c 32)/"
ssh root@lettuce -f 'mkdir -p /var/lib/dokku/data/storage/{{cookiecutter.project_slug}}/'
ssh root@lettuce -f 'chown -R dokku:dokku /var/lib/dokku/data/storage/{{cookiecutter.project_slug}}/'
ssh -t dokku@lettuce storage:mount {{cookiecutter.project_slug}} /var/lib/dokku/data/storage/{{cookiecutter.project_slug}}:/storage
ssh root@lettuce -f 'mkdir -p /home/dokku/{{cookiecutter.project_slug}}/nginx.conf.d'
ssh root@lettuce -f 'echo "location /media {" >> /home/dokku/{{cookiecutter.project_slug}}/nginx.conf.d/media.conf'
ssh root@lettuce -f 'echo "    alias /var/lib/dokku/data/storage/{{cookiecutter.project_slug}};" >> /home/dokku/{{cookiecutter.project_slug}}/nginx.conf.d/media.conf'
ssh root@lettuce -f 'echo "}" >> /home/dokku/{{cookiecutter.project_slug}}/nginx.conf.d/media.conf'
ssh root@lettuce -f 'chown -R dokku:dokku /home/dokku/{{cookiecutter.project_slug}}/nginx.conf.d/media.conf'
