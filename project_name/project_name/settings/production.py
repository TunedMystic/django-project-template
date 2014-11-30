from __future__ import absolute_import
from os.path import join, normpath
from .base import *

import imp, os

DEBUG = False

TEMPLATE_DEBUG = DEBUG

MANAGERS = ADMINS

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': os.environ['OPENSHIFT_MYSQL_DB_NAME'],
#        'USER': os.environ['OPENSHIFT_MYSQL_DB_USERNAME'],
#        'PASSWORD': os.environ['OPENSHIFT_MYSQL_DB_PASSWORD'],
#        'HOST': os.environ['OPENSHIFT_MYSQL_DB_HOST'],
#        'PORT': os.environ['OPENSHIFT_MYSQL_DB_PORT'],
#    }
#}
