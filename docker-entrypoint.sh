#!/bin/sh
find . -name '*.pyc' -delete

set -eu
sleep 2
python src/manage.py migrate
echo "done migrate"
sleep 1
python src/manage.py runserver 0.0.0.0:8000
echo "done runserver"
