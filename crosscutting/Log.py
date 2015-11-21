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
    ext = None
    field_separator = None
    file_name = None  # With extension

    def __init__(self, name, ext):
        """
        __init__(self, name, ext)
            Chooses the name of the file.
            If is a csv, also writes the header.
        """
        self.ext = '.' + ext
        if name.endswith(ext):
            self.name = name.replace(self.ext, '').strip()
            self.file_name = name
        else:
            self.name = name.strip()
            self.file_name = self.name + self.ext

        if ext == 'txt':
            self.field_separator = '\n'
        else:
            self.field_separator = ','

        self.__check_if_exists()

        # If csv, then write file header
        if self.ext is '.csv':
            f_log = open(self.file_name, 'w')
            f_log.__write('#File name, Title, Author, Creator, Subject,'
                          ' Producer, Creation date, Modification date,'
                          ' Encrypted, Pages, Size\n')
            f_log.close()

    def __check_if_exists(self):
        """
        __check_if_exists(self)
            Checks if file exists.
            If exists rename the data file.
        """

        # FIXME: Refactor this function. Really needed.
        # Dive into check_if_exists and rename

        # Check if target data file is a dir
        # It happens in the real world...
        if os.path.isdir(self.file_name):
            presentation.Messages.info_msg(self.file_name + ' is a dir.')
            # Create another data file
            self.file_name = 'pdfMetadataLog'

        # Check if log_file already exists
        if os.path.exists(self.file_name):
            presentation.Messages.info_msg(self.file_name + ' already existst.' +
                                           'Renaming data file...')

            name_flog = self.name

            # Rename the data file until does not exist
            i = 1
            while os.path.exists(name_flog + self.ext):
                name_flog = ''
                name_flog = self.name + ' (' + str(i) + ')'
                i = i + 1

            self.file_name = name_flog + self.ext

    def write(self, metadata):
        """
        write(self, metadata)
            Writes the metadata to the data file.
        Args:
            - metadata: Metadata of PDF file.
        """

        f_log = open(self.file_name, 'a+')
        self.__format_write(f_log, 'File', metadata.name)
        self.__format_write(f_log, 'Path ', metadata.abs_path)
        self.__format_write(f_log, 'Title', metadata.title)
        self.__format_write(f_log, 'Author', metadata.author)
        self.__format_write(f_log, 'Creator', metadata.creator)
        self.__format_write(f_log, 'Subject', metadata.subject)
        self.__format_write(f_log, 'Producer', metadata.producer)
        self.__format_write(f_log, 'Creation date', metadata.creation_date)
        self.__format_write(f_log, 'Modification date',
                            metadata.modification_date)
        self.__format_write(f_log, 'Encrypted', metadata.encrypted)
        self.__format_write(f_log, 'Pages', metadata.num_pages)
        self.__format_write(f_log, 'Size', metadata.size)
        f_log.write('\n')
        f_log.close()

    def __format_write(self, f_log, field, info):
        """
        __format_write(self, f_log, field_info)
            Formats the information and writes it to the data file.
        Args:
            - f_log: (file) Log file.
            - field: (string) Current information field.
            - info: (string) Information.
        """
        # FIXTHIS: With inheritance
        if info:
            if self.ext == '.txt':
                field_info = field + ': ' + info + self.field_separator
            else:
                if field is 'Size':
                    field_info = info
                else:
                    field_info = info + self.field_separator
            f_log.write(field_info)
        # If it's a empty field (None), write only the separator (',')
        elif self.ext == '.csv':
            f_log.write(self.field_separator)
