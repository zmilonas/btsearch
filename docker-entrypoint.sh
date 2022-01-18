#!/bin/sh
set -eu
sleep 5
python src/manage.py syncdb --noinput
echo "done syncdb"
sleep 2
python src/manage.py migrate --noinput
echo "done migrate"
sleep 2
python src/manage.py runserver 0.0.0.0:8000 --noinput
echo "done runserver"
