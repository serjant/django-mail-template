# -*- coding: UTF-8 -*-
from django.utils.translation import gettext_lazy as _
from django.forms import EmailField, ValidationError


class Default(dict):
    def __missing__(self, key):
        return '{' + key + '}'


def replace_context_variable(text, context_variable):
    return text.format_map(Default(**context_variable))


def clean_address_list(addresses, field_name=None):
    if (addresses is None or len(addresses) == 0) and field_name is None:
        return []
    if not isinstance(addresses, list):
        addresses = addresses.split(',')
    field_ = EmailField()
    try:
        return [field_.clean(addr) for addr in addresses]
    except ValidationError:
        raise ValidationError(_(f'Enter a valid comma separated '
                                f'list of email addresses for '
                                f'field {field_name}.'))

    # if isinstance(addresses, list):
    #     return addresses
    # if addresses is None or len(addresses) == 0:
    #     return []
    # return [address.strip() for address in addresses.split(',')]
