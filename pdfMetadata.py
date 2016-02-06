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

from application.pdf_metadata import get_metadata
from application.pdf_metadata import scan
from application.utils.python_utils import exit_signal_handler
from application.utils.python_utils import get_interpreter_version
from crosscutting.condition_messages import print_error
from crosscutting.condition_messages import print_info
from crosscutting.constants import REQUIRED_PYTHON_VERSION
from domain.log_csv import LogCsv
from domain.log_txt import LogTxt
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

        log_txt = None
        log_csv = None
        total_files = 0
        analyzed_files = 0

        if args.log:
            log_txt = LogTxt(args.log)

        if args.csv:
            log_csv = LogCsv(args.csv)

        for argument in args.arguments:
            if os.path.isfile(argument):
                total_files = total_files + 1

                metadata = get_metadata(argument)

                if metadata:
                    analyzed_files = analyzed_files + 1

                    if log_txt:
                        log_txt.write(metadata)

                    if log_csv:
                        log_csv.write(metadata)

            elif os.path.isdir(argument):
                analyzed_files, total_files = scan(
                    argument, analyzed_files, total_files, log_txt, log_csv)
            else:
                print_error(
                    '{0} is not a valid PDF file or a existing directory.'.format(argument))

        if log_txt:
            print_info('Saved to: {0}'.format(log_txt.file_name))
        if log_csv:
            print_info('Saved to: {0}'.format(log_csv.file_name))

        print_info(
            'Analyzed files: {0}/{1}'.format(analyzed_files, total_files))
    else:
        print_error('Requires Python {0}'.format(REQUIRED_PYTHON_VERSION))
        exit(0)
