release: python manage.py migrate --noinput
web: gunicorn LMKHEYAR.wsgi --timeout 60 --log-file