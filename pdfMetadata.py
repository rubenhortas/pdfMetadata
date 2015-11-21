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

from application.pdf_metadata import get_file_info
from application.pdf_metadata import scan_dir
from application.utils.python_utils import exit_signal_handler
from application.utils.python_utils import get_interpreter_version
from crosscutting import condition_messages
from crosscutting import constants
from domain.log_csv import LogCsv
from domain.log_txt import LogTxt
from domain.metadata import Metadata


if __name__ == '__main__':

    signal.signal(signal.SIGINT, exit_signal_handler)

    interpreterVersion = get_interpreter_version()

    if(interpreterVersion == constants.PYTHON_REQUIRED_VERSION):

        parser = argparse.ArgumentParser(prog='pdfMetadata')
        parser = argparse.ArgumentParser(description='Scan pdf files \
                                         looking for their metadata.')
        parser.add_argument('arguments',
                            metavar='ARGUMENTS',
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
            f_log_txt = LogTxt(args.log, 'txt')

        if args.csv:
            f_log_csv = LogCsv(args.csv, 'csv')

        for argument in args.arguments:
            if os.path.isfile(argument):
                analyzed_files = analyzed_files + 1  # FIXTHIS
                total_files = total_files + 1
                get_file_info(argument)
            elif os.path.isdir(argument):
                # FIXTHIS
                # I don't think that the counters works as expected
                analyzed_files, total_files = scan_dir(argument,
                                                       analyzed_files,
                                                       total_files)
            else:
                condition_messages.print_error(argument + ' is not a valid PDF' +
                                               ' file or a existing directory.')

        if f_log_txt:
            contidion_messages.print_info('Saved to: ' + f_log_txt.fname)
        if f_log_csv:
            condition_messages.print_info('Saved to: ' + f_log_csv.fname)

        condition_messages.print_info('Analyzed files: ' + str(analyzed_files)
                                      + '/' + str(total_files))
    else:
        condition_messages.print_error(
            'Requires Python {0}'.format(python_required_version))
        exit(0)
