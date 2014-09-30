========================
django-project-template
========================

A project template for Django 1.6 and Python3. 

This project contains the following libraries:

Python
------
#. PyMySQL (for MySQL databases)
#. Pillow (Python Image Library for Python3)
#. django-simple-captcha (for protecting comment forms)

Web
---
#. jQuery
#. Bootstrap
#. CKEditor

It has test application with home and login/logout views. 

To use this project follow these steps:

#. Create your working environment with Python 3 (http://www.it-recipes.com/articles/blog/200)
#. Install Django 
#. Create the new project using the django-project-template
#. Install additional dependencie
#. Create environment variables

*note: these instructions show creation of a project called "project_name".  You
should replace this name with the actual name of your project.*


Installing Django
=================

To install Django in the new virtual environment, run the following command::

    $ pip install django==1.6

Creating your project
=====================

To create a new Django project called 'django_project_template' using
django-project-template, run the following command::

    $ django-admin.py startproject --template=https://github.com/AnaPana/django-project-template/archive/master.zip --extension=py,js,css,html,txt project_name

Installation of Dependencies
=============================

Depending on where you are installing dependencies:

In development::

    $ pip install -r requirements/local.txt

For production::

    $ pip install -r requirements.txt

*note: We install production requirements this way because many Platforms as a
Services expect a requirements.txt file in the root of projects.*

Environment Variables
======================

DJANGO_PROJECT_HOST
DJANGO_PROJECT_PORT
LOCAL_MYSQL_DB_NAME
LOCAL_MYSQL_DB_USERNAME
LOCAL_MYSQL_DB_PASSWORD
LOCAL_MYSQL_DB_HOST
LOCAL_MYSQL_DB_PORT

For Linux add lines into your ~/.profile file:
<env_variable>=<value> && export <env_variable>
