#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    MessagesMetadata.py
"""

from presentation.color import Color
from presentation.tag import Tag


def print_file_name(print_file_name):
    print Tag.info + Color.bold_green + print_file_name + Color.end


def print_document_info(field_name, field_value):
    print Tag.info + field_name + ':\t\t' + field_value


def print_date(field_name, field_value):
    print Tag.info + field_name + ':\t' + field_value


def print_highlighted(field_name, field_value):
    print Tag.info + Color.bold_green + field_name + ':\t\t' + \
        Color.bold_red + field_value + Color.end
