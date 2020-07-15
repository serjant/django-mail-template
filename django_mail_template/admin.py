# -*- coding: UTF-8 -*-
from django.contrib import admin
from django.utils.translation import gettext as _

from django_mail_template.models import MailTemplate, Configuration


class MailTemplateAdmin(admin.ModelAdmin):

    actions = ['test_mail_template']

    def test_mail_template(self, request, queryset):
        pass

    test_mail_template.short_description = _('Test mails templates')


admin.site.register(MailTemplate, MailTemplateAdmin)

# admin.site.register(MailTemplate)
admin.site.register(Configuration)
