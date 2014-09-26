#!/bin/bash

cd `dirname $0`

for p in `pgrep -f 'manage.py runserver $MY_APP_HOST:$MY_APP_PORT'`
do
	kill $p
done

if [ -z "`pgrep -f 'manage.py runserver $MY_APP_HOST:$MY_APP_PORT'`" ]
then
	sleep 1
	nohup python ./manage.py runserver $MY_APP_HOST:$MY_APP_PORT >> ./runserver.log 2>&1 &
fi
