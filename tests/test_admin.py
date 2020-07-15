from unittest import TestCase as UnitTestCase
from unittest.mock import patch, Mock

from django.test import TestCase
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

from django_mail_template.admin import MailTemplateAdmin
from django_mail_template.models import MailTemplate, Configuration


class DjangoRegistrationAdminTest(TestCase):

    def test_mail_template_registry(self):
        # Test the class
        self.assertTrue(admin.site._registry[MailTemplate])

    def test_configuration_registry(self):
        # Test the class
        self.assertTrue(admin.site._registry[Configuration])


User = get_user_model()


class TestMailTemplateActionUnitTest(UnitTestCase):

    def setUp(self) -> None:
        self.admin_mail_template = admin.site._registry[MailTemplate]

    def test_action_test_mail_template_exists_in_actions_select(self):
        self.assertIn('test_mail_template',
                      self.admin_mail_template.actions)

    def test_method_test_mail_template_is_callable(self):
        assert callable(self.admin_mail_template.test_mail_template)

    def test_method_receive_two_parameter(self):
        # Should not fail
        self.admin_mail_template.test_mail_template(Mock(), Mock())

    def test_method_short_description(self):
        self.assertEqual(
            self.admin_mail_template.test_mail_template.short_description,
            _('Test mails templates'))
