#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://github.com/rubenhortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:      log.py
"""

import os
from crosscutting import condition_messages


# TODO: Do TXTLog and CSVLog as Log's inheritance and fix the __init__
class Log:
    """
    Class Log
        Stores the info and operations relatives to the data files.
    """
    name = None
    extension = None
    field_separator = None
    file_name = None  # Name with extension

    def __set_file_name(self, name):
        if name.endswith(self.extension):
            self.name = name.replace(self.extension, '').strip()
            self.file_name = name
        else:
            self.name = name.strip()
            self.fname = self.name + self.extension

    def __exists(self):
        """
            __exists(self)
            Checks if file exists.
        """

        file_exists = False

        # Check if target data file is a directory
        # It happens in the real world...
        if os.path.isdir(self.file_name):
            condition_messages.print_info(self.file_name + ' is a dir.')

            # Create another data file
            self.file_name = 'pdfMetadataLog'

        if os.path.exists(self.file_name):
            condition_messages.print_info(self.file_name + ' already existst.')
            file_exists = True

        return file_exists

    def __rename(self):
        """
        __rename(self)
            Renames the file until does not exist.
        """

        file_name = self.name
        i = 1

        while os.path.exists(file_name + self.extension):
            file_name = ''
            file_name = self.name + ' (' + str(i) + ')'
            i = i + 1

            self.file_name = file_name + self.extension
