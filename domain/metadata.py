import os
from PyPDF2 import PdfFileReader

from crosscutting.constants import ENCODING
from presentation import application_messages
from domain.utils.date_utils import get_date


class Metadata:
    """
    Class Metadata
        Data and operations relatives to the pdf file.
    """
    absolute_path = None
    name = None
    title = None
    author = None
    creator = None
    subject = None
    producer = None
    creation_date = None
    modification_date = None
    encrypted = None
    num_pages = None
    size = None
    keywords = None

    def __init__(self, file_abs_path):
        self.absolute_path = file_abs_path
        self.name = os.path.basename(self.absolute_path)

        application_messages.print_file_name(self.name)
        application_messages.print_field('Path', self.absolute_path)

        try:
            file = open(self.absolute_path, 'rb')
            document = PdfFileReader(file, strict=False)
            document_info = document.getDocumentInfo()

            if document_info:
                self._parse_document_info(document_info)

            self.encrypted = 'Yes' if document.getIsEncrypted() else 'No'
            self.num_pages = str(document.getNumPages())
            self.size = str(os.path.getsize(file_abs_path))
            self._get_keywords(document)
        except Exception as ex:
            if 'encode' not in str(ex):
                raise Exception(ex)

    def print_info(self):
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

    def _parse_document_info(self, document_info):
        file_name = document_info.get('/Title', None)
        if file_name:
            self.title = file_name.encode(ENCODING)

        author = document_info.get('/Author', None)
        if author:
            self.author = author.encode(ENCODING)

        creator = document_info.get('/Creator', None)
        if creator:
            self.creator = creator.encode(ENCODING)

        subject = document_info.subject
        if subject and (subject != ''):
            self.subject = subject.encode(ENCODING)

        producer = document_info.get('/Producer', None)
        if producer:
            if producer != '':
                producer = producer.strip()
                self.producer = producer.encode(ENCODING)

        creation_date = document_info.get('/CreationDate', None)
        if creation_date:
            self.creation_date = get_date(creation_date)

        modification_date = document_info.get('/ModDate', None)
        if modification_date:
            self.modification_date = get_date(modification_date)

    def _get_keywords(self, document):
        keywords = document.getXmpMetadata().pdf_keywords

        if keywords:
            self.keywords = keywords.encode(ENCODING).replace(',', ';')
