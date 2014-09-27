#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    Date.py
"""

from datetime import datetime
import re


def format_date(input_date):
    """
    format_date(input_date)
        Converts the dates of metadata to a readable format.
    Arguments:
        input_date: (string) Metadata date.
     """

    format_1 = re.compile("^D:[0-9]{14}")
    format_3 = re.compile("[0-9]{1,2}/[0-9]{1,2}/[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2}")
    format_4 = re.compile("^[a-zA-Z]{3} [a-zA-Z]{3} [0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} [0-9]{4}")

    fd = input_date

    """
    Formats:
        D:20071123033349Z
        D:20080219165253+01'00
    """
    if format_1.match(input_date):
        date_format1 = format_1.match(input_date).group(0)
        d = datetime.strptime(date_format1, "D:%Y%m%d%H%M%S")
        fd = datetime.strftime(d, "%H:%M:%S %d/%b/%Y (%a)")

    """
    Format:
        3/22/2004 18:21:23
    """
    if format_3.match(input_date):
        d = datetime.strptime(input_date, "%m/%d/%Y %H:%M:%S")
        fd = datetime.strftime(d, "%H:%M:%S %d/%b/%Y (%a)")

    """
    Format:
       Mon Mar 14 13:55:36 2005
    """
    if format_4.match(input_date):
        d = datetime.strptime(input_date, "%a %b %d %H:%M:%S %Y")
        fd = datetime.strftime(d, "%H:%M:%S %d/%b/%Y (%a)")

    return fd
