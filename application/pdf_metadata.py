import os

from domain.metadata import Metadata


def get_metadata(argument: str) -> list:
    def get_file_metadata(file: str) -> None:
        if file.lower().endswith('.pdf'):
            try:
                files_metadata.append(Metadata(file))
            except Exception as e:
                print(e)

    files_metadata = []

    if os.path.isdir(argument):
        for root, _, files in os.walk(argument):
            for file in files:
                file_absolute_path = os.path.join(root, file)
                get_file_metadata(file_absolute_path)

    elif os.path.isfile(argument):
        get_file_metadata(argument)

    return files_metadata
