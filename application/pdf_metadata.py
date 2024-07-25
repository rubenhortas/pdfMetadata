import os

from domain.metadata import Metadata


def get_files(argument: str) -> (list, list):
    """
    Returns all the files in the argument.

    If the argument is a directory, the argument is scanned recursively to get all files included in its subdirectories.
    The files are separated in two lists, depending on whether they are PDFs or not.

    If the argument is a file, the argument is returned included in its corresponding list.

    :param argument: file or directory.
    :return: (pdf_files, non_pdf_files)
    """

    def _sort_out_file(file: str) -> None:
        if file.lower().endswith('.pdf'):
            pdf_files.append(file)
        else:
            non_pdf_files.append(file)

    non_pdf_files = []
    pdf_files = []

    if os.path.isdir(argument):
        for root, _, files in os.walk(argument):
            for file in files:
                file_absolute_path = os.path.join(root, file)

                if os.path.isfile(file_absolute_path):
                    _sort_out_file(file_absolute_path)

    elif os.path.isfile(argument):
        _sort_out_file(argument)

    return pdf_files, non_pdf_files


def get_metadata(pdf_files: list) -> (list, list):
    metadata = []
    errors = []

    for pdf_file in pdf_files:
        # noinspection PyBroadException
        try:
            metadata.append(Metadata(pdf_file))
        except Exception:
            errors.append(pdf_file)

    return metadata, errors
