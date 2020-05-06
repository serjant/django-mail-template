# -*- coding: UTF-8 -*-
from smtplib import SMTPException

from django.db import models
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext
from django_mail_template.tools import replace_context_variable


class MailTemplate(models.Model):
    """
    Mail():
    """
    #: Field with destiny email address.
    to = models.CharField(
        max_length=1000, blank=True, null=True,
        help_text=_('A list with destiny email addresses separated with coma.')
    )
    #: Field with sender (from) email address.
    from_email = models.EmailField(help_text=_("Sender's email address."))
    #: Subject for the mail. Context variable can be used
    subject = models.CharField(
        max_length=140,
        help_text=_('Subject text for the mail. Context variable can be used.')
    )
    body = models.TextField(
        blank=True, null=True, max_length=5000,
        help_text=_('The content of the mail. Context variable can be used.'))

    class Meta:
        verbose_name = _('Mail Template')
        verbose_name_plural = _('Mails Templates')

    def __str__(self):
        return '{}'.format(self.subject)

    def clean(self):
        if self.to:
            to_field = forms.EmailField()
            try:
                return [to_field.clean(addr)
                        for addr in self.to.split(',')]
            except forms.ValidationError:
                raise forms.ValidationError(_('Enter a valid comma separated '
                                              'list of email addresses.'))

    def send(self, context=None):
        """
        When sending an email a set of attributes will be required.

        The required attributes are mainly dictated by django.core.mail
        used to send mail:
        * Message or body.
        * Subject.
        * Recipients list or to.
        * From email

        :param context: A dictionary with context variables to be used with
                        the subject and the message.
        :return: A tuple (result, message) where result is a boolean indicating
                 if mail could be sent or not. An a message in case the mail
                 could not be sent the message will be the reason. This could
                 have future uses if logging is implemented.
        """
        subject = self.subject
        body = self.body
        if context is None:
            pass
        elif not isinstance(context, dict):
            return False, _('The argument for send method must be a mapping.')
        else:
            subject = replace_context_variable(text=self.subject,
                                               context_variable=context)
            body = replace_context_variable(text=self.body,
                                            context_variable=context)
        try:
            result = send_mail(
                subject=subject,
                message=body,
                from_email=self.from_email,
                recipient_list=self.to
            )
            if result == 0:
                return False, _('Mail not sent.')
            elif result == 1:
                return True, _('Mail sent.')
        except SMTPException as e:
            return False, str(e)


class Configuration(models.Model):

    process = models.CharField(max_length=200)

    mail_template = models.ForeignKey(MailTemplate, on_delete=models.SET_NULL,
                                      null=True, blank=True)

    class Meta:
        verbose_name = _('Configuration')
        verbose_name_plural = _('Configurations')

    def __str__(self):
        str_ = '{} - '.format(self.process)
        if self.mail_template:
            str_ += str(self.mail_template)
        else:
            str_ += gettext('No mail template')
        return str_

    @staticmethod
    def get_mail_template(process):
        try:
            return Configuration.objects.get(process=process).mail_template
        except ObjectDoesNotExist:
            return None
