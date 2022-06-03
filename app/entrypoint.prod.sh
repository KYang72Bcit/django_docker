#!/bin/sh

while ! nc -z db 3306 ; do
    echo "Waiting for the MySQL Server"
    sleep 0.3
done

python manage.py makemigrations&&
python manage.py migrate&&
gunicorn -c gunicorn.conf.py employeeManage.wsgi:application
exec "$@"