import os

from PyPDF2 import PdfReader

from domain.utils.date_utils import get_date


class Metadata:
    """
    Class Metadata
        Data and operations relatives to the pdf file.
    """
    file_abs_path: str = None
    file_name: str = None
    title: str = None
    author: str = None
    creator: str = None
    subject: str = None
    producer: str = None
    creation_date: str = None
    modification_date: str = None
    encrypted: str = None
    num_pages: str = None
    size: str = None
    keywords: str = None

    def __init__(self, file):
        self.file_abs_path: str = file
        self.file_name: str = os.path.basename(file)

        document = PdfReader(self.file_abs_path, False)

        self.encrypted = 'Yes' if document.is_encrypted else 'No'
        self.num_pages = str(len(document.pages))
        self.size = str(os.path.getsize(file))
        self.keywords = document.xmp_metadata.pdf_keywords

        document_info = document.metadata

        if document_info:
            self.title = document_info.get('/Title', '')
            self.author = document_info.get('/Author', '')
            self.creator = document_info.get('/Creator', '')
            self.producer = document_info.get('/Producer', '')
            self.creation_date = get_date(document_info.get('/CreationDate', ''))
            self.modification_date = get_date(document_info.get('/ModDate', ''))
            self.subject = document_info.subject
