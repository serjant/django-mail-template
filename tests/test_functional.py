# -*- coding: UTF-8 -*-
"""
Use case:
Django mail template is used for sending greeting to a set of people.

Requirement to test:
 * The size of the set of people must be at least of two.
 * The mail should take at least two attachments.
"""
from django.core import mail
from django.test import TestCase

from django_mail_template.models import MailTemplate

PEOPLE_FIXTURE = [
    ('Ana', 'Smith', 'ana@domain.com'),
    ('Bob', 'Wellies', 'bob@domain.com')
]


class FunctionalDjangoMailTemplateTest(TestCase):

    def test_send_mail_to_people(self):
        mail_ = MailTemplate()
        mail_.from_email = 'test@domain.com'
        mail_.subject = 'A test subject for {first_name}'
        mail_.body = 'Hello {first_name} {last_namte}!'
        for first_name, last_name, email in PEOPLE_FIXTURE:
            mail_.to = [email]
            mail_.send(context={
                'first_name': first_name,
                'last_name': last_name
            })
        # Check for two sended mail
        email_1 = mail.outbox[0]
        email_2 = mail.outbox[1]

        # Assert content for first mail
        assert email_1.to == 'ana@domain.com'
        assert email_1.subject == 'A test subject for Ana'
        assert email_1.body == 'Hello Ana Smith!'
        assert email_1.from_email == 'test@domain.com'

        # Assert content for second mail
        assert email_2.to == 'bob@domain.com'
        assert email_2.subject == 'A test subject for Bob'
        assert email_2.body == 'Hello Bob Wellies!'
        assert email_2.from_email == 'test@domain.com'


# class FunctionalDjangoMailAttachmentsTest(TestCase):
#     pass


# class FunctionalDjangoConfigurationTest(TestCase):
#     pass
