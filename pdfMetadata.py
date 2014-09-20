#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://githug.com/rubenhortas/rhardening
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@status:    Developing
@version:   alpha
@file:      pdfMetadata.py
"""

from PyPDF2 import PdfFileReader
from datetime import datetime
import argparse
import os
import sys

class Pdf_metadata:
    """
    Class Pdf_metadata
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
        Arguments:
            - file_path: (string) Absolute file path.
        """
        self.abs_path = file_path
        self.name = os.path.basename(self.abs_path)

        # Try to open the pdf for read the metadata
        try:
            pdf_file = PdfFileReader(file(self.abs_path, 'rb'))
            self.encrypted = self.__is_encrypted(pdf_file)
            doc_info = pdf_file.getDocumentInfo()
            if doc_info:
                self.__parse_info(doc_info)
                self.__print_metadata()

        except Exception, e:
            if 'encode' not in str(e):
                message('error', self.name + ' ' + str(e))
                print

    def __is_encrypted(self, pdf_file):
        """
        __is_encrypted(self, pdf_file)
            Return if pdf_file is encrypted or not.
        Arguments:
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

    def __parse_info(self, doc_info):
        """
        __parse_info(self, doc_info)
            Parses the metadata.
        Arguments:
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
            self.creation_date = self.__format_date(c_date)

        m_date = doc_info.get('/ModDate', None)
        if m_date:
            self.modification_date = self.__format_date(m_date)

    def __format_date(self, input_date):
        """
        __format_date(self, input_date)
            Converts the dates of metadata to a readable format.
        Arguments:
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

    def __print_metadata(self):
        """
        __print_metadata(self)
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


def get_info(file_abs_path):
    """
    get_info(file_abs_path)
        Defined to use the script as a module.Is more confortable enter
        only one parameter.

    Arguments:
        - file_abs_path: (string) Absolute file path.
    """
    if os.path.isfile(file_abs_path):
        if file_abs_path.endswith('.pdf'):
            this_pdf = Pdf_metadata(file_abs_path)

        else:
            message('error', file_abs_path + ' is not a PDF file.')
    else:
        message('error', file_abs_path + ' is not a file.')


def __scan_fulldir(path, plain_log, csv_log, analyzed_files, total_files):
    """
    __scan_fulldir(dir_name, plain_log, csv_log)
        Scans an entire directory looking for pdf files to display its
        metadata.
    Arguments:
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

                this_pdf = Pdf_metadata(file_path)

                if f_log_txt:
                    f_log_txt.Write(this_pdf)
                if f_log_csv:
                    f_log_csv.Write(this_pdf)

    return analyzed_files, total_files


def scan_fulldir(path):
    """
    scan_fulldir(path)
        Defined to use the script as a module. Is more confortable enter
        only one parameter.

    Arguments:
        - path: (string) Target directory for scan.
    """
    __scan_fulldir(path, None, None, 0, 0)


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
    Arguments = parser.parse_args()

    f_log_txt = Arguments.log
    f_log_csv = Arguments.csv
    total_files = 0
    analyzed_files = 0

    if Arguments.log:
        f_log_txt = log(Arguments.log, 'txt')

    if Arguments.csv:
        f_log_csv = log(Arguments.csv, 'csv')

    for target in Arguments.targets:
        if os.path.isfile(target):
            if target.endswith('.pdf'):
                # Inc Counters
                analyzed_files = analyzed_files + 1
                total_files = total_files + 1

                this_pdf = Pdf_metadata(target)
                if f_log_txt:
                    f_log_txt.Write(this_pdf)

                if f_log_csv:
                    f_log_csv.Write(this_pdf)

            else:
                message('error', target + ' is not a PDF file.')
        elif os.path.isdir(target):
            analyzed_files, total_files = __scan_fulldir(target,
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
