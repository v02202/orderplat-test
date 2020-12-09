#!/bin/bash

cd /code/orderplat


python manage.py collectstatic --no-input
python manage.py qcluster & python manage.py runserver 0.0.0.0:8000
