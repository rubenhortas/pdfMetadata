#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    clear_screen.py
"""

import os


def clear_screen():
    """
    clear_screen()
        Clears the screen.
    """

    if "nt" in os.name:
        os.system("cls")
    elif "posix" in os.name:
        os.system("clear")
