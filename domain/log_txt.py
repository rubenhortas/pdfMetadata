#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:      Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:     rubenhortas at gmail.com
@github:      http://github.com/rubenhortas
@license:     CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:        LogTXT.py
@interpreter: python3
"""

from log import Log


class LogTxt(Log):

    def __init__(self):
        self.extension = '.txt'
        self.field_separator = '\n'
        self.name = name.replace(self.ext, '').strip()
        self.file_name = name

        if(self._Log__exists()):
            self._Log__rename()

    def write(self, metadata):
        f_log = open(self.file_name, 'a+')
        if metadata.name:
            f_log.write('File: ', metadata.name)
        if metadata.abs_path:
            f_log.write('Path: ', metadata.abs_path)
        if metadata.title:
            f_log.write('Title: ', metadata.title)
        if metadata.author:
            f_log.write('Author: ', metadata.author)
        if metadata.creator:
            f_log.write('Creator: ', metadata.creator)
        if metadata.subject:
            f_log.write('Subject: ', metadata.subject)
        if metadata.producer:
            f_log.write('Producer: ', metadata.producer)
        if metadata.creation_date:
            f_log.write('Creation date: ', metadata.creation_date)
        if metadata.modification_date:
            f_log.write('Modification date: ', metadata.modification_date)
        f_log.write('Encrypted: ', metadata.encrypted)
        if metadata.num_pages:
            f_log.write('Pages: ', metadata.num_pages)
        if metadata.size:
            f_log.write('Size: ', metadata.size)
        f_log.write('\n')
        f_log.close()
