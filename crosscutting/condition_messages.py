#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    condition_messages.py
"""

from presentation.tag import Tag


def print_error(msg):
    print('{0}{1}'.format(Tag.error, msg))


def print_warning(msg):
    print('{0}{1}'.format(Tag.warning, msg))


def print_info(msg):
    print('{0}{1}'.format(Tag.info, msg))


def print_exception(msg):
    print('{0}{1}\n'.format(Tag.exception, msg))
