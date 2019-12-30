# -*- coding: UTF-8 -*-
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

    #: Field holding the code to identify the mail configuration
    code = models.CharField(max_length=200, unique=True,
                            help_text=_('Unique code for mail template.'))
    #: Field with destiny email address.
    destiny = models.CharField(
        max_length=1000, blank=True, null=True,
        help_text=_('Coma separated list with destiny address.')
    )
    #: Field with sender (from) email address.
    sender = models.EmailField(help_text='Mail sender address.')
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
        related_name='file_to_mail',
        blank=True, null=True,
        help_text=_('Select files to be sent with the mail.')
    )

    def __str__(self):
        return '{}'.format(self.code)

    def clean(self):
        if self.destiny:
            destiny_field = forms.EmailField()
            try:
                return [destiny_field.clean(addr)
                        for addr in self.destiny.split(',')]
            except forms.ValidationError:
                raise forms.ValidationError(_('Enter a valid comma separated '
                                              'list of email addresses.'))

    # class Meta:
    #     verbose_name = 'Mail template'


