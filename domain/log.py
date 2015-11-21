#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://github.com/rubenhortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:      Log.py
"""

import os
import presentation


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

    def __exists(self):
        """
            __exists(self)
            Checks if file exists.
        """

        file_exists = False

        # Check if target data file is a directory
        # It happens in the real world...
        if os.path.isdir(self.file_name):
            presentation.Messages.info_msg(self.file_name + ' is a dir.')
            # Create another data file
            self.file_name = 'pdfMetadataLog'

        if os.path.exists(self.file_name):
            presentation.Messages.info_msg(
                self.file_name + ' already existst.')
            file_exists = True

        return file_exists

    def __rename(self):
        """
        __rename(self)
            Renames the file until does not exist.
        """

        file_name = self.name
        i = 1

        while os.path.exists(file_name + self.ext):
            file_name = ''
            file_name = self.name + ' (' + str(i) + ')'
            i = i + 1

            self.file_name = file_name + self.ext
