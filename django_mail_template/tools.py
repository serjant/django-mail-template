# -*- coding: UTF-8 -*-


class Default(dict):
    def __missing__(self, key):
        return '{' + key + '}'


def replace_context_variable(text, context_variable):
    return text.format_map(Default(**context_variable))
