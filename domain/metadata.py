import os

from PyPDF2 import PdfReader
from PyPDF2.errors import DependencyError

from domain.utils.date_utils import get_date


class Metadata:
    """
    Class Metadata
        Data and operations relatives to the pdf file.
    """
    file_abs_path: str = ''
    file_name: str = ''
    title: str = ''
    author: str = ''
    creator: str = ''
    subject: str = ''
    producer: str = ''
    creation_date: str = ''
    modification_date: str = ''
    encrypted: str = ''
    num_pages: str = ''
    size: str = ''
    keywords: str = ''

    def __init__(self, file: str):
        self.file_abs_path: str = file
        self.file_name: str = os.path.basename(file)
        self.size = str(os.path.getsize(file))

        document = PdfReader(self.file_abs_path, False)

        try:
            self.encrypted = 'Yes' if document.is_encrypted else 'No'
            self.num_pages = str(len(document.pages))
            self.title = document.metadata.get('/Title', '')
            self.keywords = document.metadata.get('/Keywords', '')
            self.author = document.metadata.get('/Author', '')
            self.creator = document.metadata.get('/Creator', '')
            self.producer = document.metadata.get('/Producer', '')
            self.creation_date = get_date(document.metadata.get('/CreationDate', ''))
            self.modification_date = get_date(document.metadata.get('/ModDate', ''))
            self.subject = document.metadata.subject
        except DependencyError:
            pass

    def to_txt(self) -> str:
        def _get_field_value(name: str, attribute: object) -> None:
            if attribute:
                data.append(f"{name}: {attribute}")

        data = []

        _get_field_value('File', self.file_name)
        _get_field_value('Path', self.file_abs_path)
        _get_field_value('Title', self.title)
        _get_field_value('Author', self.author)
        _get_field_value('Creator', self.creator)
        _get_field_value('Subject', self.subject)
        _get_field_value('Producer', self.producer)
        _get_field_value('Creation date', self.creation_date)
        _get_field_value('Modification date', self.modification_date)
        _get_field_value('Encrypted', self.encrypted)
        _get_field_value('Pages', self.num_pages)
        _get_field_value('Size', self.size)
        _get_field_value('Keywords', self.keywords)

        data.append('\n')

        return '\n'.join(data)

    def to_csv(self) -> str:
        def _get_field_value(attribute: object) -> None:
            if attribute:
                data.append(str(attribute))
            else:
                data.append('')

        # Header: File, Path, Title, Author, Creator, Subject, Producer, Creation date, Modification date, Encrypted,
        # Pages, Size, Keywords
        data = []

        _get_field_value(self.file_name)
        _get_field_value(self.file_abs_path)
        _get_field_value(self.title)
        _get_field_value(self.author)
        _get_field_value(self.creator)
        _get_field_value(self.subject)
        _get_field_value(self.producer)
        _get_field_value(self.creation_date)
        _get_field_value(self.modification_date)
        _get_field_value(self.encrypted)
        _get_field_value(self.num_pages)
        _get_field_value(self.size)
        _get_field_value(self.keywords)

        data.append('\n')

        return ','.join(data)
