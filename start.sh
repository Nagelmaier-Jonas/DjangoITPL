#!/bin/bash
#python manage.py migrate
#python manage.py syncdb --noinput
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', '', 'admin')" | python manage.py shell
#python manage.py runserver 8000
