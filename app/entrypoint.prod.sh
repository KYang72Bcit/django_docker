#!/bin/sh

while ! nc -z db 3306 ; do
    echo "Waiting for the MySQL Server"
    sleep 0.3
done

python manage.py migrate
exec "$@"