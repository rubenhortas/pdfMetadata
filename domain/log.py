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

    def _set_file_name(self, name):
        if name.endswith(self.extension):
            self.name = name.replace(self.extension, '').strip()
            self.file_name = name
        else:
            self.name = name.strip()
            self.file_name = self.name + self.extension
