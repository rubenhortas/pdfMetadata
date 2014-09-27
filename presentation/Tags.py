#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://githug.com/rubenhortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@status:    Developing
@version:   alpha
@file:      Tags.py
"""

from Colors import Color


class Tag:
    """
    Defines the tags for each message shown in the output.
    """

    error = '[' + Color.red + Color.bold + 'ERROR' + Color.end + '] '
    info = '[' + Color.green + '*' + Color.end + '] '
    warning = '[' + Color.yellow + Color.bold + 'ERROR' + Color.end + '] '
