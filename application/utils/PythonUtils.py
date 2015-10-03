#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    PythonUtils.py
"""

import signal
import signal
from sys import version_info

from crosscutting import Messages


def check_python_version(python_required_version):
    """
    Checks Python version.
    """

    major, minor, micro, releaselevel, serial = version_info
    if major != python_required_version:
        Messages.error_msg("Requires Python {0}".format(python_required_version))
        exit(1)


def exit_signal_handler(signal, frame):
    """"
    exit_signal_handler(signal, frame)
        Hadles an exit signal.
    Arguments:
        - signal: (int) number of signal.
        - frame: (string) name of the signal handler.

    * Subscribe importing "signal" library and adding:
        signal.signal(signal.SIGINT, exit_signal_handler)
    in the application main file.
    """

    print
    Messages.info_msg("Stopped")
    exit(0)
