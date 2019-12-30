# -*- coding: UTF-8 -*-


def replace_context_variable(text, context_variable):
    return text.format(**context_variable)
