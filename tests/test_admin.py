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
        self.mail_template_1 = Mock()
        self.mail_template_1.to = ''
        self.mail_template_2 = Mock()
        self.mail_template_2.to = ''
        self.mock_queryset = [self.mail_template_1, self.mail_template_2]
        self.request = Mock()

    def test_action_test_mail_template_exists_in_actions_select(self):
        self.assertIn('test_mail_template',
                      self.admin_mail_template.actions)

    def test_method_test_mail_template_is_callable(self):
        assert callable(self.admin_mail_template.test_mail_template)

    def test_method_receive_two_parameter(self):
        # Should not fail
        self.admin_mail_template.test_mail_template(
            self.request, self.mock_queryset)

    def test_method_short_description(self):
        self.assertEqual(
            self.admin_mail_template.test_mail_template.short_description,
            _('Test mails templates'))

    @patch('django_mail_template.admin.admin.ModelAdmin.message_user')
    def test_check_to_field_exist_for_each_selected_mail_template(
            self, mock_message_user
    ):
        self.mail_template_1.to = None
        self.mail_template_2.to = None
        self.admin_mail_template.test_mail_template(
            self.request, self.mock_queryset)
        assert mock_message_user.call_count == 2

    @patch('django_mail_template.admin.admin.ModelAdmin.message_user')
    def test_check_to_field_is_not_none_for_each_selected_mail_template(
            self, mock_message_user
    ):
        self.admin_mail_template.test_mail_template(
            self.request, self.mock_queryset)
        assert mock_message_user.call_count == 2

    @patch('django_mail_template.admin.messages')
    @patch('django_mail_template.admin.admin.ModelAdmin.message_user')
    def test_messagess_are_added_with_correct_parameters(
            self, mock_message_user, mock_messages
    ):
        err_msg = 'MailTemplate Test title: Do not have a email address ' \
                  'in To Field'
        self.mail_template_1.title = 'Test title'
        self.admin_mail_template.test_mail_template(
            self.request, [self.mail_template_1])
        mock_message_user.assert_called_once_with(
            self.request, err_msg, mock_messages.ERROR)

    def test_call_send_method_on_each_mail_template(self):
        self.mail_template_1.to = 'a@b.com'
        self.mail_template_2.to = 'a@b.com'
        self.admin_mail_template.test_mail_template(
            self.request, self.mock_queryset)
        self.mail_template_1.send.assert_called_once_with()
        self.mail_template_2.send.assert_called_once_with()

    def test_method_catch_problems_when_sending_mail(self):
        self.mail_template_1.to = 'a@b.com'
        self.mail_template_1.send.side_effect = Exception
        self.mail_template_2.to = 'a@b.com'
        self.mail_template_2.send.side_effect = Exception
        self.admin_mail_template.test_mail_template(
            self.request, self.mock_queryset)

    @patch('django_mail_template.admin.messages')
    @patch('django_mail_template.admin.admin.ModelAdmin.message_user')
    def test_messagess_are_added_with_correct_parameters(
            self, mock_message_user, mock_messages
    ):
        err_msg = 'MailTemplate Test title: Gives an error when trying to ' \
                  'send it: An error occurred.'
        self.mail_template_1.title = 'Test title'
        self.mail_template_1.to = 'a@b.com'
        self.mail_template_1.send.side_effect = Exception('An error occurred')
        self.admin_mail_template.test_mail_template(
            self.request, [self.mail_template_1])
        mock_message_user.assert_called_once_with(
            self.request, err_msg, mock_messages.ERROR)

    @patch('django_mail_template.admin.messages')
    @patch('django_mail_template.admin.admin.ModelAdmin.message_user')
    def test_reports_all_messages_successfully_sent(
            self, mock_message_user, mock_messages
    ):
        msg = 'Amount of successfully sent mails: 2.'
        self.mail_template_1.to = 'a@b.com'
        self.mail_template_2.to = 'a@b.com'
        self.admin_mail_template.test_mail_template(
            self.request, self.mock_queryset)
        mock_message_user.assert_called_once_with(
            self.request, msg, mock_messages.SUCCESS)
