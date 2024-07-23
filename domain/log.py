class Log(object):
    """
    Class Log
        Stores the info and operations relatives to the data files.
    """
    name: str = None
    extension: str = None
    field_separator: str = None
    file_name: str = None  # Name with extension

    def __init__(self, name: str, extension: str, separator: str) -> None:
        self.extension = extension
        self.field_separator = separator
        self._set_file_name(name)

    def _set_file_name(self, name: str) -> None:
        if name.endswith(self.extension):
            self.name = name.replace(self.extension, '').strip()
            self.file_name = name
        else:
            self.name = name.strip()
            self.file_name = self.name + self.extension
