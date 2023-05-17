#!/bin/sh

echo 'Running collectstatic...'
# python manage.py collectstatic --noinput

echo 'Applying migrations...'
python manage.py migrate

echo 'Starting server...'
gunicorn 'todos.wsgi' --bind=0.0.0.0:8000

exec "$@"
