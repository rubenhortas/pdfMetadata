#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:      Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:     rubenhortas at gmail.com
@github:      http://github.com/rubenhortas
@license:     CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:        pdf_metadata.py
@interpreter: python3
"""

import os
from crosscutting import condition_messages
from domain.metadata import Metadata


def get_file_info(file_path, analyzed_files):
    """
    get_file_info(file_path)
        Defined to use the script as a module.

    Arguments:
        - file_path: (string) Absolute file path.
        - analyzed_files: (integer) Files analyzed.
    """

    if file_path.endswith('.pdf') or file_path.endswith('.PDF'):
        analyzed_files = analyzed_files + 1

        try:
            metadata = Metadata(file_path)
            metadata.print_info()
        except Exception as ex:
            condition_messages.print_exception(ex)
    else:
        condition_messages.print_error(
            '{0} is not a PDF file.'.format(file_path))

    return analyzed_files


def scan_dir(path, analyzed_files, total_files, f_log_txt=None, f_log_csv=None):
    """
    __scan_dir(dir_name, plain_log, csv_log)
        Scans an entire directory looking for pdf files to display its
        metadata.
    Arguments:
        - path: (string) Target directory for scan.
        - analyzed_files: (integer) Files analyzed.
        - total_files: (integer) Total files analyzed.
    """

    for root, dirs, files in os.walk(path):
        for f in files:
            total_files = total_files + 1

            file_path = os.path.join(root, f)

            analyzed_files = analyzed_files + \
                get_file_info(file_path, analyzed_files)

            if f_log_txt:
                f_log_txt.write(metadata)
            if f_log_csv:
                f_log_csv.write(metadata)

    return analyzed_files, total_files
