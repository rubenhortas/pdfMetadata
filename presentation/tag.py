#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://githug.com/rubenhortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@status:    Developing
@version:   alpha
@file:      Tag.py
"""

from presentation.Color import Color


class Tag:
    """
    Defines the tags for each message shown in the output.
    """

    error = "[{0}ERROR{1}]".format(Color.bold_red, Color.end)
    exception = "[{0}EXCEPTION{1}]".format(Color.bold_red, Color.end)
    info = "[{0}*{1}]".format(Color.green, Color.end)
    warning = "[{0}Warning{1}]".format(Color.bold_orange, Color.end)
