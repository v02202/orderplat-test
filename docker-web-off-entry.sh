#!/bin/bash

cd /code/orderplat


python manage.py collectstatic --no-input

python manage.py qcluster & gunicorn --bind 0.0.0.0:8001 --workers=2 --timeout 60 orderplat.wsgi:application
