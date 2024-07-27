import multiprocessing
import os
from multiprocessing import Pool

from domain.metadata import Metadata


def get_files(paths: list) -> (list, list):
    """
    Returns all the files in the arguments.

    If the argument is a directory, the argument is scanned recursively to get all files included in its subdirectories.
    The files are separated in two lists, depending on whether they are PDFs or not.

    If the argument is a file, the argument is returned included in its corresponding list.

    :param paths: file or directory.
    :return: (pdf_files, non_pdf_files)
    """

    def _sort_out_file(file: str) -> None:
        if file.lower().endswith('.pdf'):
            pdf_files.append(file)
        else:
            non_pdf_files.append(file)

    non_pdf_files = []
    pdf_files = []

    for path in paths:
        if os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    file_absolute_path = os.path.join(root, file)

                    if os.path.isfile(file_absolute_path):
                        _sort_out_file(str(file_absolute_path))

        elif os.path.isfile(path):
            _sort_out_file(path)

        else:
            non_pdf_files.append(path)

    return pdf_files, non_pdf_files


def get_metadata(pdf_files: list):
    with Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(_get_metadata, pdf_files)

    metadata = []
    errors = []

    for result in results:
        if result[0]:
            metadata.append(result[0])
        if result[1]:
            errors.append(result[1])

    return metadata, errors


def write_log_txt(file: str, metadata_files: list) -> None:
    with open(file, 'w') as f:
        for metadata in metadata_files:
            f.write(metadata.to_txt())


def write_log_csv(file: str, metadata_files: list) -> None:
    with open(file, 'w') as f:
        f.write('File, Path, Title, Author, Creator, Subject, Producer, Creation date, Modification date, '
                'Encrypted, Pages, Size, Keywords\n')

        for metadata in metadata_files:
            f.write(metadata.to_csv())


def _get_metadata(file: str) -> (Metadata | None, str | None):
    metadata = None
    error = None

    # noinspection PyBroadException
    try:
        metadata = Metadata(file)
    except Exception:
        error = file

    return metadata, error
