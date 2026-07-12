import multiprocessing
from multiprocessing import Pool
from pathlib import Path

from domain.metadata import Metadata


def get_files(paths: list) -> tuple:
    """
    Returns all the files in the arguments.

    If the argument is a directory, the argument is scanned recursively to get all files included in its subdirectories.
    The files are separated in two lists, depending on whether they are PDFs or not.

    If the argument is a file, the argument is returned included in its corresponding list.

    :param paths: file or directory.
    :return: (pdf_files, non_pdf_files)
    """

    pdf_files = []
    non_pdf_files = []

    def _sort_out_file(file_path: Path) -> None:
        if file_path.suffix.lower() == ".pdf":
            pdf_files.append(str(file_path.resolve()))
        else:
            non_pdf_files.append(str(file_path.resolve()))

    for path_str in paths:
        p = Path(path_str)

        if p.is_dir():
            for file_path in p.rglob('*'):
                if file_path.is_file():
                    _sort_out_file(file_path)

        elif p.is_file():
            _sort_out_file(p)

        else:
            # Si no existe o no es ni archivo ni directorio, lo guardamos como string original
            non_pdf_files.append(path_str)

    return pdf_files, non_pdf_files


def get_metadata(pdf_files: list) -> tuple:
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
    with open(file, "w") as f:
        for metadata in metadata_files:
            f.write(metadata.to_txt())


def write_log_csv(file: str, metadata_files: list) -> None:
    with open(file, "w") as f:
        f.write(
            "File, Path, Title, Author, Creator, Subject, Producer, Creation date, Modification date, "
            "Encrypted, Pages, Size, Keywords\n"
        )

        for metadata in metadata_files:
            f.write(metadata.to_csv())


def _get_metadata(file: str) -> tuple:
    metadata = None
    error = None

    # noinspection PyBroadException
    try:
        metadata = Metadata(file)
    except Exception:
        error = file

    return metadata, error
