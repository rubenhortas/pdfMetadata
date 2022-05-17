#!/usr/bin/env python
# _*_ coding:utf-8 _*
from presentation.tag import Tag


def print_error(msg):
    print('{0}{1}\n'.format(Tag.error, msg))


def print_warning(msg):
    print('{0}{1}'.format(Tag.warning, msg))


def print_info(msg):
    print('{0}{1}'.format(Tag.info, msg))


def print_exception(msg):
    print('{0}{1}\n'.format(Tag.exception, msg))
