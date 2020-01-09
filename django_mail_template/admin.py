from django.contrib import admin
from django_mail_template.models import MailTemplate, Configuration

admin.site.register(MailTemplate)
admin.site.register(Configuration)
