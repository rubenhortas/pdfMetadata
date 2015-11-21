#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:      Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:     rubenhortas at gmail.com
@github:      http://github.com/rubenhortas
@license:     CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:        log__txt.py
@interpreter: python3
"""

from log import Log


class LogTxt(Log):

    def __init__(self, name):
        self.extension = '.txt'
        self.field_separator = '\n'

        self._Log__set_file_name(name)

        if(self._Log__exists()):
            self._Log__rename()

    def write(self, metadata):
        try:
            f_log = open(self.file_name, 'a+')
            if metadata.name:
                f_log.write('File: {0}'.format(metadata.name))
            if metadata.abs_path:
                f_log.write('Path: {0}'.format(metadata.abs_path))
            if metadata.title:
                f_log.write('Title: {0}'.format(metadata.title))
            if metadata.author:
                f_log.write('Author: {0}'.format(metadata.author))
            if metadata.creator:
                f_log.write('Creator: {0}'.format(metadata.creator))
            if metadata.subject:
                f_log.write('Subject: {0}'.format(metadata.subject))
            if metadata.producer:
                f_log.write('Producer: {0}'.format(metadata.producer))
            if metadata.creation_date:
                f_log.write(
                    'Creation date: {0}'.format(metadata.creation_date))
            if metadata.modification_date:
                f_log.write(
                    'Modification date: {0}'.format(metadata.modification_date))
            f_log.write('Encrypted: {0}'.format(metadata.encrypted))
            if metadata.num_pages:
                f_log.write('Pages: {0}'.format(metadata.num_pages))
            if metadata.size:
                f_log.write('Size: {0}'.format(metadata.size))
            f_log.write('\n')
            f_log.close()
        except Exception as ex:
            condition_messages.print_exception(ex)
