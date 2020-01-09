# -*- coding: UTF-8 -*-
SECRET_KEY = 'django-mail-template'

INSTALLED_APPS = [
    'django_mail_template',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

ROOT_URLCONF = 'tests.urls'

import os
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))
LOCALE_PATHS = [
    os.path.join(BASE_DIR, "django_mail_template/locale"),
]
