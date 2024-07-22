import os
from presentation.condition_messages import print_info


class Log(object):
    """
    Class Log
        Stores the info and operations relatives to the data files.
    """
    name = None
    extension = None
    field_separator = None
    file_name = None  # Name with extension

    def __init__(self, name, extension, separator):
        self.extension = extension
        self.field_separator = separator
        self._set_file_name(name)

        if self._exists():
            self._rename()

    def _set_file_name(self, name):
        if name.endswith(self.extension):
            self.name = name.replace(self.extension, '').strip()
            self.file_name = name
        else:
            self.name = name.strip()
            self.file_name = self.name + self.extension

    def _exists(self):
        exists = False

        # Check if target data file is a directory
        # It happens in the real world...
        if os.path.isdir(self.file_name):
            print_info(f"{self.file_name} is a directory")

            # Create another data file
            self.file_name = 'pdfMetadataLog'

        if os.path.exists(self.file_name):
            print_info(f"{self.file_name} already exists")
            exists = True

        return exists

    def _rename(self):
        file_name = self.name + self.extension
        i = 1

        while os.path.exists(file_name):
            file_name = f"{self.name} ({i}){self.extension}"
            i = i + 1

        self.file_name = file_name
