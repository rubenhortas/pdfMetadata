#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    Messages.py
"""

from presentation.Tag import Tag


def print_error(msg):
    print Tag.error + msg


def print_warning(msg):
    print Tag.warning + msg


def print_info(msg):
    print Tag.info + msg


def print_exception(msg):
    print Tag.exception + msg
