#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    Messages.py
"""

import Tags


def error_msg(msg):
    print Tags.Tag.error + msg


def warning_msg(msg):
    print Tags.Tag.warning + msg


def info_msg(msg):
    print Tags.Tag.info + msg
