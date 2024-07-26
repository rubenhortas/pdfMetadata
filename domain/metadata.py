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
