from django.test import TestCase
from django.contrib import admin

from django_mail_template.models import MailTemplate, Configuration


class DjangoMailTemplateAdminTest(TestCase):

    def test_mail_template_registry(self):
        # Test the class
        assert admin.site._registry[MailTemplate]

    def test_configuration_registry(self):
        # Test the class
        assert admin.site._registry[Configuration]
