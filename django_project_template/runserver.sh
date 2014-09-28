#!/bin/bash

cd `dirname $0`

for p in `pgrep -f 'manage.py runserver $DJANGO_PROJECT_HOST:$DJANGO_PROJECT_PORT --settings="django_template_project.settings.local"'`
do
	kill $p
done

if [ -z "`pgrep -f 'manage.py runserver $DJANGO_PROJECT_HOST:$DJANGO_PROJECT_PORT --settings="django_template_project.settings.local"'`" ]
then
	sleep 1
	nohup python ./manage.py runserver $DJANGO_PROJECT_HOST:$DJANGO_PROJECT_PORT --settings="django_template_project.settings.local" >> ./runserver.log 2>&1 &
fi
