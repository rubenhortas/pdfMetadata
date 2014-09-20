#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:     Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:    rubenhortas at gmail.com
@github:     http://githug.com/rubenhortas/
@license:    CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:       Log.py
"""


class Log:
    """
    Class log
        Stores the info and operations relatives to the log files.
    """
    name = None  # name
    ext = None  # ext
    sep = None  # field separator
    fname = None  # name.ext

    def __init__(self, name, ext):
        """
        __init__(self, name, ext)
            Chooses the name of the file.
            If is a csv, also writes the header.
        """
        self.ext = '.' + ext
        if name.endswith(ext):
            self.name = name.replace(self.ext, '').strip()
            self.fname = name
        else:
            self.name = name.strip()
            self.fname = self.name + self.ext

        if ext == 'txt':
            self.sep = '\n'
        else:
            self.sep = ','

        self.__check_if_exists()

        # If csv, then write file header
        if self.ext is '.csv':
            f_log = open(self.fname, 'w')
            f_log.__write('#File name, Title, Author, Creator, Subject,'
                          ' Producer, Creation date, Modification date,'
                          ' Encrypted, Pages, Size\n')
            f_log.close()

    def __check_if_exists(self):
        """
        __check_if_exists(self)
            Checks if file exists.
            It exists, rename the log file.
        """
        # Check if target log file is a dir
        # It happens in real world...
        if os.path.isdir(self.fname):
            message('info', self.fname + ' is a dir.')
            # Create another log file
            self.fname = 'pdfMetadataLog'

        # Check if log_file already exists
        if os.path.exists(self.fname):
            message('info', self.fname + ' already existst. Renaming ' +
                    'log file...')

            name_flog = self.name

            # Rename the log file until does not exist
            i = 1
            while os.path.exists(name_flog + self.ext):
                name_flog = ''
                name_flog = self.name + ' (' + str(i) + ')'
                i = i + 1

            self.fname = name_flog + self.ext

    def write(self, pdf):
        """
        write(self, pdf)
            Writes the info of the pdf (metadata) to the log file.
        Args:
            - pdf: (pdf_metadata) Metadata of PDF.
        """
        f_log = open(self.fname, 'wa')
        self.__format_write(f_log, 'File', pdf.name)
        self.__format_write(f_log, 'Title', pdf.title)
        self.__format_write(f_log, 'Author', pdf.author)
        self.__format_write(f_log, 'Creator', pdf.creator)
        self.__format_write(f_log, 'Subject', pdf.subject)
        self.__format_write(f_log, 'Producer', pdf.producer)
        self.__format_write(f_log, 'Creation date', pdf.creation_date)
        self.__format_write(f_log, 'Modification date',
                            pdf.modification_date)
        self.__format_write(f_log, 'Encrypted', pdf.encrypted)
        self.__format_write(f_log, 'Pages', pdf.num_pages)
        self.__format_write(f_log, 'Size', pdf.size)
        f_log.write('\n')
        f_log.close()

    def __format_write(self, f_log, field, info):
        """
        __format_write(self, f_log, field_info)
            Formats the information and writes it to the log file.
        Args:
            - f_log: (file) Log file.
            - field: (string) Current information field.
            - info: (string) Information.
        """
        if info:
            if self.ext == '.txt':
                field_info = field + ': ' + info + self.sep
            else:
                if field is 'Size':
                    field_info = info
                else:
                    field_info = info + self.sep
            f_log.write(field_info)
        # If it's a empty field (None), write only the separator (',')
        elif self.ext == '.csv':
            f_log.write(self.sep)
