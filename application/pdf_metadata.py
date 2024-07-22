import os
from presentation.condition_messages import print_error
from presentation.condition_messages import print_exception
from domain.log_csv import LogCsv
from domain.log_txt import LogTxt
from domain.metadata import Metadata


def scan(path: str, analyzed_files: int, total_files: int, log_txt: LogTxt | None = None,
         log_csv: LogCsv | None = None):
    """
    scan(path, analyzed_files, total_files, f_log_txt, f_log_csv)
        Scans an entire directory looking for pdf files to display its metadata.

    :param path: path: Path to scan.
    :param analyzed_files: Files analyzed.
    :param total_files: Total files analyzed.
    :param log_txt: txt log file.
    :param log_csv: csv log file.
    :return: analyzed_files (files with metadata)
    :return: total_files (total scanned files)
    """
    for root, dirs, files in os.walk(path):
        for file in files:
            total_files += 1
            file_path = os.path.join(root, file)
            metadata = get_metadata(file_path)

            if metadata:
                analyzed_files += 1

                if log_txt:
                    log_txt.write(metadata)

                if log_csv:
                    log_csv.write(metadata)

    return analyzed_files, total_files


def get_metadata(file_path: str) -> Metadata:
    """
     get_metadata(file_path)
        Gets the metadata from a pdf file.

    :param file_path: Absolute file path.
    :return: Metadata | None
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
