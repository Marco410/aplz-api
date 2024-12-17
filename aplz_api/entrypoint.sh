#!/bin/sh

echo 'Running collecstatic...'
python manage.py collectstatic --no-input --settings=aplz_api.settings

echo 'Applying migrations...'
python manage.py wait_for_db --settings=aplz_api.settings
python manage.py migrate --settings=aplz_api.settings

echo 'Running server...'

gunicorn --env DJANGO_SETTINGS_MODULE=aplz_api.settings aplz_api.wsgi:application --bind 0.0.0.0:$PORT  --timeout 72000 
