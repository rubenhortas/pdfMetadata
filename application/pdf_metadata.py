# def scan(path: str, analyzed_files: int, total_files: int, log_txt: LogTxt | None = None,
#          log_csv: LogCsv | None = None):
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             total_files += 1
#             file_path = os.path.join(root, file)
#             metadata = get_metadata(file_path)
#
#             if metadata:
#                 analyzed_files += 1
#
#                 if log_txt:
#                     log_txt.write(metadata)
#
#                 if log_csv:
#                     log_csv.write(metadata)
#
#     return analyzed_files, total_files
#
#
# def get_metadata(file_path: str) -> Metadata:
#     metadata = None
#
#     if file_path.lower().endswith('.pdf'):
#         try:
#             metadata = Metadata(file_path)
#             metadata.print_info()
#         except Exception as e:
#             print_exception(str(e))
#     else:
#         print_error('{0} is not a PDF file.'.format(file_path))
#
#     return metadata
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
