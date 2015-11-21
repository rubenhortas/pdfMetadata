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

from application.PDFMetadata import get_file_info
from application.PDFMetadata import scan_dir
from application.utils.PythonUtils import exit_signal_handler
from application.utils.PythonUtils import get_interpreter_version
from crosscutting import Constants
from crosscutting import Messages
from crosscutting.Log import Log
from domain.Metadata import Metadata


if __name__ == '__main__':

    signal.signal(signal.SIGINT, exit_signal_handler)

    interpreterVersion = get_interpreter_version()

    if(interpreterVersion == Constants.REQUIRED_PYTHON_VERSION):

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
            f_log_txt = Log(args.log, 'txt')

        if args.csv:
            f_log_csv = Log(args.csv, 'csv')

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
                Messages.error_msg(argument + ' is not a valid PDF' +
                                   ' file or a existing directory.')

        if f_log_txt:
            Messages.info_msg('Saved to: ' + f_log_txt.fname)
        if f_log_csv:
            Messages.info_msg('Saved to: ' + f_log_csv.fname)

        Messages.info_msg('Analyzed files: ' + analyzed_files
                          + '/' + total_files)
    else:
        Messages.error_msg(
            'Requires Python {0}'.format(python_required_version))
        exit(0)
