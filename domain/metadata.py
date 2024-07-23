import os

from PyPDF2 import PdfFileReader, DocumentInformation

from crosscutting.constants import ENCODING
from domain.utils.date_utils import get_date
from presentation import application_messages


class Metadata:
    """
    Class Metadata
        Data and operations relatives to the pdf file.
    """
    absolute_path: str = None
    name: str = None
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

    def __init__(self, file_abs_path):
        try:
            self.absolute_path = file_abs_path
            self.name = os.path.basename(self.absolute_path)

            application_messages.print_file_name(self.name)
            application_messages.print_field('Path', self.absolute_path)

            with open(file_abs_path, 'r') as file:
                document = PdfFileReader(file, strict=False)

                self.encrypted = 'Yes' if document.getIsEncrypted() else 'No'
                self.num_pages = str(document.getNumPages())
                self.size = str(os.path.getsize(file_abs_path))
                self._get_keywords(document)

                document_info = document.getDocumentInfo()

                if document_info:
                    self._get_document_info(document_info)
        except UnicodeEncodeError:
            pass
        except Exception:
            raise Exception

    def print_info(self) -> None:
        """
        print_info(self)
            Displays the metadata in a nice format.
        """
        if self.title:
            application_messages.print_field('Title', self.title)

        if self.author:
            application_messages.print_field_highlighted('Author', self.author)

        if self.creator:
            application_messages.print_field('Creator', self.creator)

        if self.subject:
            application_messages.print_field('Subject', self.subject)

        if self.producer:
            application_messages.print_field('Producer', self.producer)

        if self.creation_date:
            application_messages.print_field('Creation date', self.creation_date)

        if self.modification_date:
            application_messages.print_field('Modification date', self.modification_date)

        if self.encrypted:
            if self.encrypted == 'Yes':
                application_messages.print_field_highlighted('Encrypted', self.encrypted)
            else:
                application_messages.print_field('Encrypted', self.encrypted)

        if self.num_pages:
            application_messages.print_field('Pages', self.num_pages)

        if self.size:
            application_messages.print_field('Size', '{0} bytes'.format(self.size))

        if self.keywords:
            application_messages.print_field('Keywords', self.keywords)

        print()

    def _get_document_info(self, document_info: DocumentInformation) -> None:
        title = document_info.get('/Title', '')
        if title:
            self.title = str(title.encode('UTF-8'))

        author = document_info.get('/Author', '')
        if author:
            self.author = str(author.encode(ENCODING))

        creator = document_info.get('/Creator', '')
        if creator:
            self.creator = str(creator.encode(ENCODING))

        subject = document_info.subject
        if subject:
            self.subject = str(subject.encode(ENCODING))

        producer = document_info.get('/Producer', '')
        if producer:
                self.producer = str(producer.encode(ENCODING))

        creation_date = document_info.get('/CreationDate', '')
        if creation_date:
            self.creation_date = get_date(creation_date)

        modification_date = document_info.get('/ModDate', '')
        if modification_date:
            self.modification_date = get_date(modification_date)

    def _get_keywords(self, document: PdfFileReader) -> None:
        keywords = document.getXmpMetadata().pdf_keywords

        if keywords:
            self.keywords = keywords.encode(ENCODING).replace(',', ';')
