class Log(object):
    """
    Class Log
        Stores the info and operations relatives to the data files.
    """
    file_name: str = None
    extension: str = None

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name if file_name.endswith(self.extension) else f"{file_name}.{self.extension}"
