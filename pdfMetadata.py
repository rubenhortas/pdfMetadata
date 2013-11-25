#!/usr/bin/env python
#_*_ coding: utf-8 _*_

"""
File:       pdfMetadata.py
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
        Colors the text to display it in the output.
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
        Defines the tags for each message type shown in the ouput.
    """

    file_name = '[*] '
    info = '\t[+]'
    info_green = '\t[' + color.bold_red + '+' + color.end + ']'
    info_msg = '[!]'
    error = '[' + color.red + color.bold + '+' + color.end + ']'


class pdf_metadata:
    """
    Class pdf_metadata
        Stores the data relative to the pdf (metadata, pages, size...).
    """

    def __init__(self, name, title, author, creator, subject, producer,
                 c_date, m_date, encrypted, num_pages, file_size):

        self.name = name
        self.title = title
        self.author = author
        self.creator = creator
        self.subject = subject
        self.producer = producer
        self.creation_date = c_date
        self.modification_date = m_date
        self.encrypted = encrypted
        self.num_pages = num_pages
        self.size = file_size


def __Print_error(err_msg):
    """
    __Print_error(err_msg)
        Prints error messages.
    Args:
        - err_msg: (string) Error message.
    """

    print tag.error + color.bold_red + 'ERROR: ' + color.end + \
        str(err_msg)


def __Print_info(info_msg):
    """
    __Print_info(info_msg)
        Prints information messages.
    Args:
        - info_msg: (string) Information message.
    """

    print tag.info_msg + color.bold_green + 'INFO: ' + color.end + \
        str(info_msg)


def __Parse_doc_info(doc_info):
    """
    __Parse_doc_info(doc_info)
        Parses and formats the doc_info list.
    Args:
        - doc_info: (list) This list contais the metadata of the pdf.
    """

    if doc_info is not None:

        title = doc_info.get('/Title', None)

        author = doc_info.get('/Author', None)

        creator = doc_info.get('/Creator', None)

        if doc_info.subject != '':
            subject = doc_info.subject
        else:
            subject = None

        producer = doc_info.get('/Producer', None)
        producer = producer.strip()
        if producer == '':
            producer = None

        c_date_ini = doc_info.get('/CreationDate', None)
        if c_date_ini is not None:
            c_date = __Format_date(c_date_ini)
        else:
            c_date = None

        m_date_ini = doc_info.get('/ModDate', None)
        if m_date_ini is not None:
            m_date = __Format_date(m_date_ini)
        else:
            m_date = None

        return title, author, creator, subject, producer, \
            c_date, m_date
    else:
        return None, None, None, None, None, None, None


def __Print_metadata(pdf):
    """
    __Print_metadata(pdf)
        Displays formatted pdf metadata.
    Args:
        - pdf: (pdf_metadata) Stores pdf information (metadata,
        size, pages...).
    """

    print tag.file_name + color.bold_green + str(pdf.name) + color.end

    if pdf.title is not None:
        print tag.info + 'Title:\t\t%s' % pdf.title

    if pdf.author is not None:
        print tag.info_green + 'Autor:\t\t' + color.bold_red \
            + unicode(pdf.author) + color.end

    if pdf.creator is not None:
        print tag.info + 'Creator:\t\t' + unicode(pdf.creator)

    if pdf.subject is not None:
        print tag.info + 'Subject:\t\t' + unicode(pdf.subject)

    if pdf.producer is not None:
        print tag.info + 'Producer:\t\t' + unicode(pdf.producer)

    if pdf.creation_date is not None:
        print tag.info + 'Creation date:\t' + str(pdf.creation_date)

    if pdf.modification_date is not None:
        print tag.info + 'Modification date:\t' \
            + str(pdf.modification_date)

    print tag.info + 'Encrypted:\t\t%s' % pdf.encrypted

    print tag.info + 'Pages:\t\t' + str(pdf.num_pages)

    print tag.info + 'Size:\t\t' + str(pdf.size) + ' bytes'

    print


def Log(name, pdf, log_file, log_format):
    """
    Log(name, pdf, log_file, log_format)
        Writes the ouput to a log file.
    Args:
        - name: (string) pdf name.
        - pdf: (pdf_metadata) File metadata obtained.
        - log_file: (string) Log name entered by the user.
        - log_format: (string) Type of log.
                - 'txt' -> Logs to a plain text file.
                - 'csv' -> Logs to a csv file.
    """

    if log_format is 'txt':
        sep = '\n'
    elif log_format is 'csv':
        sep = ','

    f_log = open(log_file, 'ab')

    #Write metadata
    __Write_to_file(f_log, 'File', name, log_format, sep)
    __Write_to_file(f_log, 'Author', pdf.author, log_format, sep)
    __Write_to_file(f_log, 'Creator', pdf.creator, log_format, sep)
    __Write_to_file(f_log, 'Subject', pdf.subject, log_format, sep)
    __Write_to_file(f_log, 'Producer', pdf.producer, log_format, sep)
    __Write_to_file(f_log, 'Creation date', pdf.creation_date,
                    log_format, sep)
    __Write_to_file(f_log, 'Modification date', pdf.modification_date,
                    log_format, sep)
    __Write_to_file(f_log, 'Encrypted', pdf.encrypted, log_format, sep)
    __Write_to_file(f_log, 'Pages', str(pdf.num_pages), log_format, sep)
    __Write_to_file(f_log, 'Size', str(pdf.size), log_format, sep)
    f_log.write('\n')

    f_log.close()


def __Log_checks(log_file, log_format):
    """
    __Log_checks(log_file, log_format)
        Does a few basic checks about file log.
    Args:
        - log_file: (string) Log name entered by the user.
        - log_format: (string) Type of log.
                - 'txt' -> Logs to a plain text file.
                - 'csv' -> Logs to a csv file.
    """

    ext = '.' + log_format

    #Check if target log_file is a dir
    #It happens in real world...
    if os.path.isdir(log_file):
        __Print_info(log_file + ' is a dir')
        log_file = 'pdfMetadata_log'

    #Check if log_file already exists
    if os.path.exists(log_file) or os.path.exists(log_file + ext):
        __Print_info(log_file + ' already exists. Renaming file log...')

        if log_file.endswith(ext):
            l_log_file = log_file.split('.', 2)
            name_log_file = l_log_file[0]
        else:
            name_log_file = log_file

        #Rename the file log until does not exist
        i = 1
        while os.path.exists(log_file) or os.path.exists(log_file + ext):
            log_file = name_log_file + '(' + str(i) + ')'
            i = i + 1

    #Add extension of log (if the user has not introduced)
    if not log_file.endswith(ext):
        log_file = log_file + ext
    return log_file


def __Write_to_file(f_log, name_info, info, log_format, sep):
    """
    __Write_to_file(f_log, name_info, info, log_format, sep)
        Writes a line in the log file.
    Args:
        - f_log: (file) Log file.
        - name_info: (string) Name field of information
                     (title, author, creator...).
        - info: (string) Metadata information.
        - log_format: (string) Type of log.
                - 'txt' -> Logs to a plain text file.
                - 'csv' -> Logs to a csv file.
        - sep: (string) Field separator in the log file.

    """

    if info is not None:
        if log_format is 'txt':
            f_log.write(name_info + ': ' + info + sep)
        if log_format is 'csv':
            if name_info is not 'Size':
                f_log.write(info + sep)
            else:
                f_log.write(info)
    elif log_format is 'csv':
            f_log.write(sep)


def __Format_date(input_date):
    """
    __Format_date(input_date)
        Converts a pdf date to a readable format
        (HH:MM:SS dd/MONTH/YY (day_of_the_week)).
    Args:
        - input_date: (string) A date extrated of the pdf metadata.
    """

    input_date = input_date.split('+', input_date.count('+'))
    tmp_date = datetime.strptime(input_date[0], "D:%Y%m%d%H%M%S")
    date = datetime.strftime(tmp_date, "%H:%M:%S %d/%b/%Y (%a)")

    return date


def __Get_info(file_path, plain_log, csv_log, analyzed_files, total_files):
    """
    __Get_info(file_path)
        Opens the pdf file for reading.
    Args:
        - file_path: (string) Absolute file path.
        - plain_log: (None | string) Log file in plain text.
        - csv_log: (None | string) Log file in csv format.
    """

    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)

    encrypted = 'No'

    try:  # Try to open not password encrypted pdf files and pdf files
          # encrypted with a blank password.
        pdf_file = PdfFileReader(file(file_path, 'rb'))
        if pdf_file.getIsEncrypted() is True:
            dec_res = pdf_file.decrypt('')
            if dec_res == 1:
                encrypted = 'Yes'

        #Get and parse metadata
        doc_info = pdf_file.getDocumentInfo()
        title, author, creator, subject, producer, c_date, m_date \
            = __Parse_doc_info(doc_info)

        num_pages = pdf_file.getNumPages()

        #Group info
        pdf_meta = pdf_metadata(file_name, title, author, creator,
                                subject, producer, c_date, m_date,
                                encrypted, num_pages, file_size)

        __Print_metadata(pdf_meta)

        if plain_log:
            Log(file_name, pdf_meta, plain_log, 'txt')
        if csv_log:
            Log(file_name, pdf_meta, f_log_csv, 'csv')

        analyzed_files = analyzed_files + 1

    except Exception, e:
        error = file_name + ' ' + str(e)
        __Print_error(error)

    finally:
        total_files = total_files + 1
        return analyzed_files, total_files


def Get_info(file_path):
    """
    Defined to use the script as a module. Is more confortable enter
        only one parameter.

    Get_info(file_path)
        Opens the pdf file for reading.
    Args:
        - file_path: (string) Absolute file path.
    """
    __Get_info(file_path, None, None, 0, 0)


def __Scan_fulldir(path, plain_log, csv_log, analyzed_files, total_files):
    """
    __Scan_fulldir(dir_name, plain_log, csv_log)
        Scans an entire directory looking for pdf files to display its
        metadata.
    Args:
        - dir_name: (string) Target directory for scan.
        - plain_log: (None | string) Log file in plain text.
        - csv_log: (None | string) Log file in csv format.
    """
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith('.pdf'):
                file_path = os.path.join(root, f)
                analyzed_files, total_files = __Get_info(file_path,
                                                         plain_log,
                                                         csv_log,
                                                         analyzed_files,
                                                         total_files)

    return analyzed_files, total_files


def Scan_fulldir(path):
    """
    Defined to use the script as a module. Is more confortable enter
        only one parameter.

    Scan_fulldir(dir_name)
        Scans an entire directory looking for pdf files to display its
        metadata.
    Args:
        - dir_name: (string) Target directory for scan.
    """
    __Scan_fulldir(path, None, None, 0, 0)


if __name__ == '__main__':

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

    total_files = 0
    analyzed_files = 0

    if args.log is not None:
        f_log_txt = __Log_checks(args.log, 'txt')
    else:
        f_log_txt = None

    if args.csv is not None:
        f_log_csv = __Log_checks(args.csv, 'csv')
        f_log = open(f_log_csv, 'w')
        f_log.write('#File name, Author, Creator, Subject, Producer, ' +
                    'Creation date, Modification date, Encrypted,' +
                    ' Pages, Size\n')
        f_log.close
    else:
        f_log_csv = None

    for target in args.targets:
        if os.path.isfile(target):
            if target.endswith('.pdf'):
                analyzed_files, total_files = __Get_info(target,
                                                         f_log_txt,
                                                         f_log_csv,
                                                         analyzed_files,
                                                         total_files)
            else:
                __Print_error(target + ' is not a PDF file.')
        elif os.path.isdir(target):
            analyzed_files, total_files = __Scan_fulldir(target,
                                                         f_log_txt,
                                                         f_log_csv,
                                                         analyzed_files,
                                                         total_files)
        else:
            __Print_error(target + ' is not a valid PDF file or a \
                        existing directory.')

        if f_log_txt is not None:
            __Print_info('Saved to: ' + f_log_txt)
        if f_log_csv is not None:
            __Print_info('Saved to: ' + f_log_csv)

        __Print_info('Analyzed files: ' + str(analyzed_files) + '/' +
                     str(total_files) + '.')
