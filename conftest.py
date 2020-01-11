import os
import django
import pytest
from django.conf import settings


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings_test')
os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'


def pytest_configure():
    settings.LANGUAGE_CODE = 'en'
    settings.DEBUG = False
    django.setup()


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass

