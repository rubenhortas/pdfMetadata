#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://github.com/rubenhortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:      pdfMetadata.py
"""

import argparse
import os
import signal
import sys

from application.utils.PythonUtils import check_python_version
from application.utils.PythonUtils import exit_signal_handler
from crosscutting import Messages
from crosscutting.Log import Log
from domain.PDFMetadata import PDFMetadata


def get_info(file_abs_path):
    """
    get_info(file_abs_path)
        Defined to use the script as a module.

    Arguments:
        - file_abs_path: (string) Absolute file path.
    """

    if os.path.isfile(file_abs_path):
        if file_abs_path.endswith('.pdf'):
                PDFMetadata(file_abs_path)

        else:
            Messages.error_msg(file_abs_path +
                               ' is not a PDF file.')
    else:
        Messages.error_msg(file_abs_path + 'is not a file.')


def __scan_fulldir(path, analyzed_files, total_files):
    """
    __scan_fulldir(dir_name, plain_log, csv_log)
        Scans an entire directory looking for pdf files to display its
        metadata.
    Arguments:
        - path: (string) Target directory for scan.
        - analyzed_files: (integer) Files analyzed.
        - total_files: (integer) Total files analyzed.
    """

    try:
        for root, dirs, files in os.walk(path):
            for f in files:
                if f.endswith('.pdf'):
                    file_path = os.path.join(root, f)

                    analyzed_files = analyzed_files + 1
                    total_files = total_files + 1

                    this_pdf = PDFMetadata(file_path)

                    if f_log_txt:
                        f_log_txt.write(this_pdf)
                    if f_log_csv:
                        f_log_csv.write(this_pdf)

        return analyzed_files, total_files
    except KeyboardInterrupt:
        sys.exit(0)


def scan_fulldir(path):
    """
    scan_fulldir(path)
        Defined to use the script as a module.
    Arguments:
        - path: (string) Target directory for scan.
    """

    __scan_fulldir(path, None, None, 0, 0)


if __name__ == '__main__':

    python_required_version = 2

    check_python_version(python_required_version)

    signal.signal(signal.SIGINT, exit_signal_handler)

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
        f_log_txt = Log(args.log, 'txt')

    if args.csv:
        f_log_csv = Log(args.csv, 'csv')

    for target in args.targets:
        if os.path.isfile(target):
            if target.endswith('.pdf'):
                try:
                    this_pdf = PDFMetadata(target)
                    if f_log_txt:
                        f_log_txt.Write(this_pdf)

                    if f_log_csv:
                        f_log_csv.Write(this_pdf)
                except Exception, e:
                    Messages.error_msg(e)
                    analyzed_files = analyzed_files + 1
                finally:
                    total_files = total_files + 1
            else:
                Messages.error_msg(target + 'is not a PDF file.')

        elif os.path.isdir(target):
            analyzed_files, total_files = __scan_fulldir(target,
                                                         analyzed_files,
                                                         total_files)
        else:
            Messages.error_msg(target + ' is not a valid PDF' +
                               ' file or a existing directory.')

        if f_log_txt:
            Messages.info_msg('Saved to: ' + f_log_txt.fname)
        if f_log_csv:
            Messages.info_msg('Saved to: ' + f_log_csv.fname)

        Messages.info_msg('Analyzed files: ' + str(analyzed_files)
                          + '/' + str(total_files))
