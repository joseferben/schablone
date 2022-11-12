#!/bin/bash
set -e

# Restore the database if it does not already exist.
if [ -f $DB_FILE ]; then
  echo "Database already exists, skipping restore"
else
  echo "No database found, restoring from replica if exists"
  litestream restore -v -if-replica-exists -o $DB_FILE "${REPLICA_URL}"
fi

python manage.py migrate
python manage.py run_huey &
litestream replicate -exec "gunicorn config.wsgi:application -b 0.0.0.0:8080 --capture-output --enable-stdio-inheritance" $DB_FILE "${REPLICA_URL}"
