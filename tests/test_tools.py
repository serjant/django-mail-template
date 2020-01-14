# -*- coding: UTF-8 -*-
from unittest import TestCase as UnitTest

from django_mail_template.tools import replace_context_variable


class TestReplaceContextVariable(UnitTest):
    """
    There are 6 test for almost 5 lines code.
    """

    def test_second_parameter_must_be_dictionary(self):
        with self.assertRaises(TypeError):
            replace_context_variable('', '')
        with self.assertRaises(TypeError):
            replace_context_variable('', [])
        with self.assertRaises(TypeError):
            replace_context_variable('', 1)
        replace_context_variable('', {})

    def test_first_parameter_must_be_string(self):
        with self.assertRaises(AttributeError):
            replace_context_variable([], {})
        with self.assertRaises(AttributeError):
            replace_context_variable(1, {})
        with self.assertRaises(AttributeError):
            replace_context_variable({}, {})
        replace_context_variable('', {})

    def test_return_main_text_with_variables_replaced(self):
        text = 'Dummy text {context_variable}.'
        expected = 'Dummy text example.'
        data = {'context_variable': 'example'}
        assert expected == replace_context_variable(text, data)

    def test_return_main_text_with_multiple_variables_replaced(self):
        text = 'Dummy text {context_variable} {replaced_text}.'
        expected = 'Dummy text example of replace.'
        data = {'context_variable': 'example', 'replaced_text': 'of replace'}
        assert expected == replace_context_variable(text, data)

    def test_return_valid_value_without_all_variable_mapping(self):
        text = 'Dummy text {context_variable}.'
        expected = 'Dummy text example.'
        data = {'context_variable': 'example', 'replaced_text': 'of replace'}
        assert expected == replace_context_variable(text, data)

    def test_return_valid_value_without_context_variable_in_text(self):
        text = 'Dummy text {context_variable} {fake%2d0} {more-fake}.'
        expected = 'Dummy text example {fake%2d0} {more-fake}.'
        data = {'context_variable': 'example', 'replaced_text': 'of replace'}
        assert expected == replace_context_variable(text, data)
