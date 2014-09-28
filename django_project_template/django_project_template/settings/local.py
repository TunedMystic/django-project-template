"""Development settings and globals."""
from __future__ import absolute_import
from os.path import join, normpath
from .base import *

import os

DEBUG = True

TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['LOCAL_MYSQL_DB_NAME'],
        'USER': os.environ['LOCAL_MYSQL_DB_USERNAME'],
        'PASSWORD': os.environ['LOCAL_MYSQL_DB_PASSWORD'],
        'HOST': os.environ['LOCAL_MYSQL_DB_HOST'],
        'PORT': os.environ['LOCAL_MYSQL_DB_PORT'],
    }
}


# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
        'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# See: http://django-debug-toolbar.readthedocs.org/en/latest/installation.html#explicit-setup
INSTALLED_APPS += (
                   'debug_toolbar',
)
MIDDLEWARE_CLASSES += (
                       'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PATCH_SETTINGS = False

# http://django-debug-toolbar.readthedocs.org/en/latest/installation.html
INTERNAL_IPS = ('127.0.0.1',)
