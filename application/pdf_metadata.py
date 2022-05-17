#!/usr/bin/env python
# _*_ coding:utf-8 _*
import os
from crosscutting.condition_messages import print_error
from crosscutting.condition_messages import print_exception
from domain.metadata import Metadata


def get_metadata(file_path):
    """
    get_metadata(file_path)
        Defined to use the script as a module.

    Arguments:
        file_path: (string) Absolute file path.
    """

    metadata = None

    if file_path.lower().endswith('.pdf'):
        try:
            metadata = Metadata(file_path)
            metadata.print_info()
        except Exception as ex:
            print_exception(ex)
    else:
        print_error('{0} is not a PDF file.'.format(file_path))

    return metadata


def scan(path, analyzed_files, total_files, f_log_txt=None, f_log_csv=None):
    """
    scan(path, analyzed_files, total_files, f_log_txt, f_log_csv)
        Scans an entire directory looking for pdf files to display its
        metadata.
    Arguments:
        path: (string) Target directory for scan.
        analyzed_files: (integer) Files analyzed.
        total_files: (integer) Total files analyzed.
        f_log_txt: (string) txt log file.
        f_log_csv: (string) csv log file.
    """

    for root, dirs, files in os.walk(path):
        for f in files:
            total_files = total_files + 1

            file_path = os.path.join(root, f)

            metadata = get_metadata(file_path)

            if metadata:
                analyzed_files = analyzed_files + 1

                if f_log_txt:
                    f_log_txt.write(metadata)
                if f_log_csv:
                    f_log_csv.write(metadata)

    return analyzed_files, total_files
