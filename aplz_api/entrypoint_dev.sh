#!/bin/sh

python manage.py makemigrations --no-input
python manage.py migrate

# python manage.py collectstatic --noinput

exec "$@"