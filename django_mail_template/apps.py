from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DjangoMailTemplateConfig(AppConfig):
    name = 'django_mail_template'
    verbose_name = _('Django Mail Template')
    default_auto_field = 'django.db.models.BigAutoField'
