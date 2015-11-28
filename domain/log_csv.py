#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:      Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:     rubenhortas at gmail.com
@github:      http://github.com/rubenhortas
@license:     CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:        log_csv.py
@interpreter: python3
"""

from crosscutting import condition_messages
from log import Log


class LogCsv(Log):

    def __init__(self, name):
        self.extension = '.csv'
        self.field_separator = ','

        self._set_file_name(name)

        if self._exists():
            self._rename()

        self.__write_header()

    def __write_header(self):
        """
        __write_header(self)
            Writes CSV file header.
        """

        try:
            f_log = open(self.file_name, 'w')
            f_log.write('#File name, Title, Author, Creator, Subject,'
                        ' Producer, Creation date, Modification date,'
                        ' Encrypted, Pages, Size\n')
            f_log.close()
        except Exception as ex:
            condition_messages.print_exception(ex)

    def write(self, metadata):
        try:
            f_log = open(self.file_name, 'a+')
            if metadata.name:
                f_log.write(metadata.name)
            f_log.write(self.field_separator)
            if metadata.abs_path:
                f_log.write(metadata.abs_path)
            f_log.write(self.field_separator)
            if metadata.title:
                f_log.write(metadata.title)
            f_log.write(self.field_separator)
            if metadata.author:
                f_log.write(metadata.author)
            f_log.write(self.field_separator)
            if metadata.creator:
                f_log.write(metadata.creator)
            f_log.write(self.field_separator)
            if metadata.subject:
                f_log.write(metadata.subject)
            f_log.write(self.field_separator)
            if metadata.producer:
                f_log.write(metadata.producer)
            f_log.write(self.field_separator)
            if metadata.creation_date:
                f_log.write(metadata.creation_date)
            f_log.write(self.field_separator)
            if metadata.modification_date:
                f_log.write(metadata.modification_date)
            f_log.write(self.field_separator)
            f_log.write(metadata.encrypted)
            f_log.write(self.field_separator)
            if metadata.num_pages:
                f_log.write(metadata.num_pages)
            f_log.write(self.field_separator)
            if metadata.size:
                f_log.write(metadata.size)
            f_log.write('\n')
            f_log.close()
        except Exception as ex:
            condition_messages.print_exception(ex)
