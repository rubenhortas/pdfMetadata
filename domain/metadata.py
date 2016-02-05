#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    metadata.py
"""

from PyPDF2 import PdfFileReader
import os
import Date as Date
from crosscutting import application_messages


class Metadata:
    """
    Class Metadata
        Dta and operations relatives to the pdf file.
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
    coding = 'UTF-8'

    def __init__(self, file_abs_path):
        """
        __init__(self, file_abs_path):

        Arguments:
            - file_abs_path: (string) Absolute file path.
        """

        self.absolute_path = file_abs_path
        self.name = os.path.basename(self.absolute_path)

        application_messages.print_file_name(self.name)
        application_messages.print_document_info('Path', self.absolute_path)

        try:
            document = PdfFileReader(file(self.absolute_path, 'rb'))

            self.__get_encrypted_status(document)

            document_info = document.getDocumentInfo()
            if document_info:
                self.__parse_document_info(document_info)

        except Exception as ex:
            if 'encode' not in str(ex):
                raise Exception(ex)

    def print_info(self):
        """
        print_info(self)
            Displays the metadata in a nice format.
        """

        if self.title:
            application_messages.print_document_info('Title', self.title)

        if self.author:
            application_messages.print_highlighted('Author', self.author)

        if self.creator:
            application_messages.print_document_info('Creator', self.creator)

        if self.subject:
            application_messages.print_document_info('Subject', self.subject)

        if self.producer:
            application_messages.print_document_info('Producer', self.producer)

        if self.creation_date:
            application_messages.print_date(
                'Creation date', self.creation_date)

        if self.modification_date:
            application_messages.print_date('Modification date',
                                            self.modification_date)

        if self.encrypted:
            if self.encrypted == 'Yes':
                application_messages.print_highlighted(
                    'Encrypted', self.encrypted)
            else:
                application_messages.print_document_info(
                    'Encrypted', self.encrypted)

        if self.num_pages:
            application_messages.print_document_info('Pages', self.num_pages)

        if self.size:
            application_messages.print_document_info(
                'Size', '{0} bytes'.format(self.size))
        print

    def __get_encrypted_status(self, document):
        """
        __get_encrypted_status(self, document)
            Return if document is encrypted or not.
        Arguments:
            - document: (pdfFileReader) PDF file.
        """

        if document.getIsEncrypted() is True:
            self.encrypted = 'Yes'
        else:
            self.encrypted = 'No'

    def __parse_document_info(self, document_info):
        """
        __parse_document_info(self, document_info)
            Parses the document info (metadata).
        Arguments:
            - document_info: (pdfFileReader.getDocumentInfo()) Metadata.
        """

        file_name = document_info.get('/Title', None)
        if file_name:
            self.title = file_name.encode(self.coding)

        author = document_info.get('/Author', None)
        if author:
            self.author = author.encode(self.coding)

        creator = document_info.get('/Creator', None)
        if creator:
            self.creator = creator.encode(self.coding)

        subject = document_info.subject
        if subject and (subject != ''):
            self.subject = subject.encode(self.coding)

        producer = document_info.get('/Producer', None)
        if producer:
            if producer != '':
                producer = producer.strip()
                self.producer = producer.encode(self.coding)

        creation_date = document_info.get('/CreationDate', None)
        if creation_date:
            self.creation_date = Date.format_date(creation_date)

        modification_date = document_info.get('/ModDate', None)
        if modification_date:
            self.modification_date = Date.format_date(modification_date)
