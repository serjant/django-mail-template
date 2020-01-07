# -*- coding: UTF-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext as _
from django.db import models
from email.utils import getaddresses, formataddr

from django import forms


# Create your models here.
class MailAttachment(models.Model):
    """

    """
    #: File to be attached to mail.
    file = models.FileField(
        help_text=_('File to be attached to a mail template.')
    )


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
    from_email = models.EmailField(help_text="Sender's email address.")
    #: Subject for the mail. Context variable can be used
    subject = models.CharField(
        max_length=140,
        help_text=_('Subject text for the mail. Context variable can be used.'))
    body = models.CharField(
        blank=True, null=True, max_length=5000,
        help_text=_('The content of the mail. Context variable can be used.'))
    #: Field with the files attached to the mail.
    attachments = models.ManyToManyField(
        to=MailAttachment,
        blank=True, null=True,
        help_text=_('Select files to be sent with the mail.')
    )

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


class Configuration(models.Model):

    process = models.CharField(max_length=200)

    mail_template = models.ForeignKey(MailTemplate, on_delete=models.SET_NULL,
                                      null=True, blank=True)

    def __str__(self):
        str_ = '{} - '.format(self.process)
        if self.mail_template:
            str_ += str(self.mail_template)
        else:
            str_ += _('No mail template')
        return str_

    @staticmethod
    def get_mail_template(process):
        try:
            return Configuration.objects.get(process=process).mail_template
        except ObjectDoesNotExist:
            return None
