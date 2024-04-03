#!/bin/bash

python manage.py makemigrations

python manage.py migrate

python manage.py loaddata fixtures/data_dump.json

flake8 apps

python manage.py runserver 0.0.0.0:8000



