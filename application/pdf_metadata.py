#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:      Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:     rubenhortas at gmail.com
@github:      http://github.com/rubenhortas
@license:     CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:        PDFMetadata.py
@interpreter: python3
"""

import os
from crosscutting import Messages
from domain.metadata import Metadata


def get_file_info(file_abs_path):
    """
    get_file_info(file_abs_path)
        Defined to use the script as a module.

    Arguments:
        - file_abs_path: (string) Absolute file path.
    """

    if os.path.isfile(file_abs_path):
        if file_abs_path.endswith('.pdf'):
            metadata = Metadata(file_abs_path)
            metadata.print_info()
        else:
            Messages.error_msg(file_abs_path +
                               ' is not a PDF file.')
    else:
        Messages.error_msg(file_abs_path + 'is not a file.')


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

    try:
        for root, dirs, files in os.walk(path):
            for f in files:
                if f.endswith('.pdf'):
                    file_path = os.path.join(root, f)

                    analyzed_files = analyzed_files + 1
                    total_files = total_files + 1

                    metadata = Metadata(file_path)
                    metadata.print_info()

                    if f_log_txt:
                        f_log_txt.write(metadata)
                    if f_log_csv:
                        f_log_csv.write(metadata)

        return analyzed_files, total_files
    except KeyboardInterrupt:
        sys.exit(0)
