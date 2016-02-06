#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    python_utils.py
"""

from sys import version_info
from crosscutting.condition_messages import print_info


def get_interpreter_version():
    """
    get_interpreter_version()
        Gets the current version of the python interpreter.
    """

    major, minor, micro, release, serial = version_info
    return major


def exit_signal_handler(signal, frame):
    """"
    exit_signal_handler(signal, frame)
        Handles an exit signal.
    Arguments:
        signal: (int) number of signal.
        frame: (string) name of the signal handler.
    """

    print
    print_info("Stopped")
    exit(0)
