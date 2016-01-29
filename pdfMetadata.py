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
from crosscutting.constants import REQUIRED_PYTHON_VERSION
from domain.log_csv import LogCsv
from domain.log_txt import LogTxt
from domain.metadata import Metadata
from presentation.utils.screen import clear_screen


if __name__ == '__main__':

    signal.signal(signal.SIGINT, exit_signal_handler)

    clear_screen()

    interpreter_version = get_interpreter_version()

    if interpreter_version == REQUIRED_PYTHON_VERSION:

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

        log_txt = args.log
        log_csv = args.csv
        total_files = 0
        analyzed_files = 0

        if args.log:
            log_txt = LogTxt(args.log)

        if args.csv:
            log_csv = LogCsv(args.csv)

        for argument in args.arguments:
            if os.path.isfile(argument):
                total_files = total_files + 1

                metadata = get_file_info(argument)

                if metadata:
                    analyzed_files = analyzed_files + 1

            elif os.path.isdir(argument):
                analyzed_files, total_files = scan_dir(argument,
                                                       analyzed_files,
                                                       total_files,
                                                       log_txt,
                                                       log_csv)
            else:
                condition_messages.print_error(
                    '{0} is not a valid PDF file or a existing directory.'.format(argument))

        if log_txt:
            condition_messages.print_info(
                'Saved to: {0}'.format(log_txt.file_name))
        if log_csv:
            condition_messages.print_info(
                'Saved to: {0}'.format(log_csv.file_name))

        condition_messages.print_info(
            'Analyzed files: {0}/{1}'.format(analyzed_files, total_files))
    else:
        condition_messages.print_error(
            'Requires Python {0}'.format(REQUIRED_PYTHON_VERSION))
        exit(0)
