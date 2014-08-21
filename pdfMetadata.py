#!/usr/bin/env python
#_*_ coding: utf-8 _*_

"""
File:       pdfMetadata.py
Version:    2.0
Author:     Rubén Hortas <rubenhortas@gmail.com>
Website:    http://rubenhortas.blogspot.com.es
Github:     http://github.com/rubenhortas/pdfmetadata
License:    CC BY-NC-SA 3.0
            http://creativecommons.org/licenses/by-nc-sa/3.0/
"""

import argparse
import os
import sys
from PyPDF2 import PdfFileReader
from datetime import datetime


class color:
    """
    Class color
        Colorizes the text to display in the output.
    """
    bold = '\033[1m'
    green = '\033[32m'
    bold_green = '\033[1m\033[32m'
    red = '\033[31m'
    bold_red = '\033[1m\033[31m'
    end = '\033[0m'


class tag:
    """
    Class tag
        Defines the tags for each message shown in the output.
    """
    file_name = '[*] '
    info = '\t[+]'
    info_green = '\t[' + color.bold_red + '+' + color.end + ']'
    info_msg = '[!]'
    error = '[' + color.red + color.bold + '+' + color.end + ']'


class pdf_metadata:
    """
    Class pdf_metadata
        Stores the data and operations relatives to the pdf
        (metadata, pages, size...).
    """
    abs_path = None
    name = None
    title = None
    author = None
    creator = None
    subject = None
    producer = None
    creation_date = None
    modification_date = None
    encrypted = None
    num_pages = None
    size = None

    def __init__(self, file_path):
        """
        __init__(self, file_path):
            - Try to open the pdf.
            - Get the metadata.
            - Print the metadata.
        Args:
            - file_path: (string) Absolute file path.
        """
        self.abs_path = file_path
        self.name = os.path.basename(self.abs_path)

        # Try to open the pdf for read the metadata
        try:
            pdf_file = PdfFileReader(file(self.abs_path, 'rb'))
            self.encrypted = self.__Is_encrypted(pdf_file)
            doc_info = pdf_file.getDocumentInfo()
            if doc_info:
                self.__Parse_info(doc_info)
                self.__Print_metadata()

        except Exception, e:
            if 'encode' not in str(e):
                message('error', self.name + ' ' + str(e))
                print

    def __Is_encrypted(self, pdf_file):
        """
        __Is_encrypted(self, pdf_file)
            Return if pdf_file is encrypted or not.
        Args:
            - pdf_file: (pdfFileReader) PDF file.
        """
        if pdf_file.getIsEncrypted:
            # Try to open pdf files encrypted with a blank password
            try:
                pdf_file.decrypt('')
            except Exception, e:
                pass
            finally:
                return 'Yes'
        else:
            return 'No'

    def __Parse_info(self, doc_info):
        """
        __Parse_info(self, doc_info)
            Parses the metadata.
        Args:
            - doc_info: (pdfFileReader.getDocumentInfo()) Metadata.
        """
        title = doc_info.get('/Title', None)
        if title:
            self.title = title.encode('utf-8')

        author = doc_info.get('/Author', None)
        if author:
            self.author = author.encode('utf-8')

        creator = doc_info.get('/Creator', None)
        if creator:
            self.creator = creator.encode('utf-8')

        subject = doc_info.subject
        if subject and (subject != ''):
            self.subject = subject.encode('utf-8')

        producer = doc_info.get('/Producer', None)
        if producer:
            if producer != '':
                producer = producer.strip()
                self.producer = producer.encode('utf-8')

        c_date = doc_info.get('/CreationDate', None)
        if c_date:
            self.creation_date = self.__Format_date(c_date)

        m_date = doc_info.get('/ModDate', None)
        if m_date:
            self.modification_date = self.__Format_date(m_date)

    def __Format_date(self, input_date):
        """
        __Format_date(self, input_date)
            Converts the dates of metadata to a readable format.
        Args:
            input_date: (string) Metadata date.
        """
        try:
            if '+' in input_date:
                str_date = input_date.split('+',
                                            input_date.count('+'))[0]

            elif '-' in input_date:
                str_date = input_date.split('-',
                                            input_date.count('-'))[0]
            elif 'Z' in input_date:
                str_date = input_date.split('Z')[0]
            else:
                str_date = input_date

            d = datetime.strptime(str_date, "D:%Y%m%d%H%M%S")
            formated_date = datetime.strftime(d, "%H:%M:%S %d/%b/%Y (%a)")

            return formated_date

        except Exception, e:
            print '-> input_date:', input_date
            message('date error', str(e))
            print
            return None

    def __Print_metadata(self):
        """
        __Print_metadata(self)
            Displays the metadata in a nice format.
        """

        print tag.file_name + color.bold_green + str(self.name) + \
            color.end

        print tag.info + 'Path:\t\t%s' % self.abs_path

        if self.title:
            print tag.info + 'Title:\t\t%s' % self.title

        if self.author:
            print tag.info_green + 'Author:\t\t' + color.bold_red \
                + self.author + color.end

        if self.creator:
            print tag.info + 'Creator:\t\t' + self.creator

        if self.subject:
            print tag.info + 'Subject:\t\t' + self.subject

        if self.producer:
            print tag.info + 'Producer:\t\t' + self.producer

        if self.creation_date:
            print tag.info + 'Creation date:\t' + self.creation_date

        if self.modification_date:
            print tag.info + 'Modification date:\t' \
                + self.modification_date

        print tag.info + 'Encrypted:\t\t%s' % self.encrypted

        if self.num_pages:
            print tag.info + 'Pages:\t\t' + self.num_pages

        if self.size:
            print tag.info + 'Size:\t\t' + self.size + ' bytes'

        print


class log:
    """
    Class log
        Stores the info and operations relatives to the log files.
    """
    name = None     # name
    ext = None      # ext
    sep = None      # field separator
    fname = None    # name.ext

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

        self.__Check_if_exists()

        # If csv, then write file header
        if self.ext is '.csv':
            f_log = open(self.fname, 'w')
            f_log.__write('#File name, Title, Author, Creator, Subject,'
                          ' Producer, Creation date, Modification date,'
                          ' Encrypted, Pages, Size\n')
            f_log.close()

    def __Check_if_exists(self):
        """
        __Check_if_exists(self)
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

    def Write(self, pdf):
        """
        Write(self, pdf)
            Writes the info of the pdf (metadata) to the log file.
        Args:
            - pdf: (pdf_metadata) Metadata of PDF.
        """
        f_log = open(self.fname, 'wa')
        self.__Format_write(f_log, 'File', pdf.name)
        self.__Format_write(f_log, 'Title', pdf.title)
        self.__Format_write(f_log, 'Author', pdf.author)
        self.__Format_write(f_log, 'Creator', pdf.creator)
        self.__Format_write(f_log, 'Subject', pdf.subject)
        self.__Format_write(f_log, 'Producer', pdf.producer)
        self.__Format_write(f_log, 'Creation date', pdf.creation_date)
        self.__Format_write(f_log, 'Modification date',
                            pdf.modification_date)
        self.__Format_write(f_log, 'Encrypted', pdf.encrypted)
        self.__Format_write(f_log, 'Pages', pdf.num_pages)
        self.__Format_write(f_log, 'Size', pdf.size)
        f_log.write('\n')
        f_log.close()

    def __Format_write(self, f_log, field, info):
        """
        __Format_write(self, f_log, field_info)
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


class message:
    """
    Class message
        Stores and displays an information (or error) message.
    """
    msg = None
    msg_type = None

    def __init__(self, msg_type, msg):
        """
        __init__(self, msg_type, msg)
            Stores and displays a message.
        Args:
            - msg_type: (string) Type of the message.
                        - information
                        - error
            - msg: (string) Message.
        """
        self.msg_type = msg_type
        self.msg = msg
        self.Print_msg()

    def Print_msg(self):
        """
        Print_msg(self)
            Displays the message in a nice format.
        """
        if self.msg_type == 'error':
            print tag.error + color.bold_red + 'Error: ' + color.end \
                + self.msg
        else:
            print tag.info_msg + color.bold_green + 'INFO: ' \
                + color.end + self.msg


def Get_info(file_abs_path):
    """
    Get_info(file_abs_path)
        Defined to use the script as a module.Is more confortable enter
        only one parameter.

    Args:
        - file_abs_path: (string) Absolute file path.
    """
    if os.path.isfile(file_abs_path):
        if file_abs_path.endswith('.pdf'):
            this_pdf = pdf_metadata(file_abs_path)

        else:
            message('error', file_abs_path + ' is not a PDF file.')
    else:
        message('error', file_abs_path + ' is not a file.')


def __Scan_fulldir(path, plain_log, csv_log, analyzed_files, total_files):
    """
    __Scan_fulldir(dir_name, plain_log, csv_log)
        Scans an entire directory looking for pdf files to display its
        metadata.
    Args:
        - dir_name: (string) Target directory for scan.
        - plain_log: (None | string) Log file in plain text.
        - csv_log: (None | string) Log file in csv format.
        - analyzed_files: (integer) Files analyzed.
        - total_files: (integer) Total files analyzed.
    """
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith('.pdf'):
                file_path = os.path.join(root, f)

                # Inc counters
                analyzed_files = analyzed_files + 1
                total_files = total_files + 1

                this_pdf = pdf_metadata(file_path)

                if f_log_txt:
                    f_log_txt.Write(this_pdf)
                if f_log_csv:
                    f_log_csv.Write(this_pdf)

    return analyzed_files, total_files


def Scan_fulldir(path):
    """
    Scan_fulldir(path)
        Defined to use the script as a module. Is more confortable enter
        only one parameter.

    Args:
        - path: (string) Target directory for scan.
    """
    __Scan_fulldir(path, None, None, 0, 0)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='pdfMetadata')
    parser = argparse.ArgumentParser(description='Scan pdf files \
                                     looking for their metadata.')
    parser.add_argument('targets',
                        metavar='TARGET',
                        nargs='+',
                        help='file[s] or path[s] to scan pdf files')
    parser.add_argument('--log', metavar='log file', nargs='?',
                        help='Saves the output into a plain text file.')
    parser.add_argument('--csv', metavar='csv file', nargs='?',
                        help='Saves the output into a csv file.')
    args = parser.parse_args()

    f_log_txt = args.log
    f_log_csv = args.csv
    total_files = 0
    analyzed_files = 0

    if args.log:
        f_log_txt = log(args.log, 'txt')

    if args.csv:
        f_log_csv = log(args.csv, 'csv')

    for target in args.targets:
        if os.path.isfile(target):
            if target.endswith('.pdf'):
                # Inc Counters
                analyzed_files = analyzed_files + 1
                total_files = total_files + 1

                this_pdf = pdf_metadata(target)
                if f_log_txt:
                    f_log_txt.Write(this_pdf)

                if f_log_csv:
                    f_log_csv.Write(this_pdf)

            else:
                message('error', target + ' is not a PDF file.')
        elif os.path.isdir(target):
            analyzed_files, total_files = __Scan_fulldir(target,
                                                         f_log_txt,
                                                         f_log_csv,
                                                         analyzed_files,
                                                         total_files)
        else:
            message('error', target + ' is no t a valid PDF file' +
                    'or a existing directory.')

        if f_log_txt:
            message('info', 'Saved to: ' + f_log_txt.fname)
        if f_log_csv:
            message('info', 'Saved to: ' + f_log_csv.fname)

        # Report message
        message('info', 'Analyzed files: ' + str(analyzed_files) + '/' +
                str(total_files) + '.')
