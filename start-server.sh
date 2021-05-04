#!/usr/bin/env bash
# start-server.sh
echo "Starting..."
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (ls -ls; python manage.py migrate; python manage.py createsuperuser --no-input; python manage.py collectstatic --noinput)
fi
(ls -l; gunicorn cookbook.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
#(python manage.py runserver 0.0.0.0:8010) &
nginx -g "daemon off;"