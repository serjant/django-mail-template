# -*- coding: UTF-8 -*-
SECRET_KEY = 'django-mail-template'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django_mail_template.apps.DjangoMailTemplateConfig',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

import os
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))
LOCALE_PATHS = [
    os.path.join(BASE_DIR, "django_mail_template/locale"),
]
