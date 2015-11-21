#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    Metadata.py
"""

from PyPDF2 import PdfFileReader
import os
import Date as Date
from crosscutting import application_messages
from crosscutting import condition_messages


class Metadata:
    """
    Class Metadata
        Dta and operations relatives to the pdf file.
    """

    abs_path = None
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
    char_encoding = 'UTF-8'

    def __init__(self, file_abs_path):
        """
        __init__(self, file_abs_path):

        Arguments:
            - file_abs_path: (string) Absolute file path.
        """

        self.abs_path = file_abs_path
        self.name = os.path.basename(self.abs_path)

        try:
            document = PdfFileReader(file(self.abs_path, 'rb'))

            self.encrypted = self.__is_encrypted(document)

            document_info = document.getDocumentInfo()
            if document_info:
                self.__parse_document_info(document_info)

        except Exception, ex:
            if 'encode' not in str(ex):
                condition_messages.print_exception(ex)

    def __is_encrypted(self, document):
        """
        __is_encrypted(self, document)
            Return if document is encrypted or not.
        Arguments:
            - document: (pdfFileReader) PDF file.
        """

        if document.getIsEncrypted():
            try:
                document.decrypt('')
            except Exception:
                pass
            finally:
                return True
        else:
            return False

    def __parse_document_info(self, document_info):
        """
        __parse_document_info(self, document_info)
            Parses the document info (metadata).
        Arguments:
            - document_info: (pdfFileReader.getDocumentInfo()) Metadata.
        """

        file_name = document_info.get('/Title', None)
        if file_name:
            self.title = file_name.encode(self.char_encoding)

        author = document_info.get('/Author', None)
        if author:
            self.author = author.encode(self.char_encoding)

        creator = document_info.get('/Creator', None)
        if creator:
            self.creator = creator.encode(self.char_encoding)

        subject = document_info.subject
        if subject and (subject != ''):
            self.subject = subject.encode(self.char_encoding)

        producer = document_info.get('/Producer', None)
        if producer:
            if producer != '':
                producer = producer.strip()
                self.producer = producer.encode(self.char_encoding)

        creation_date = document_info.get('/CreationDate', None)
        if creation_date:
            self.creation_date = Date.format_date(creation_date)

        modification_date = document_info.get('/ModDate', None)
        if modification_date:
            self.modification_date = Date.format_date(modification_date)

    def print_info(self):
        """
        print_info(self)
            Displays the metadata in a nice format.
        """

        application_messages.print_file_name(self.name)
        application_messages.print_document_info('Path', self.abs_path)

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
            application_messages.print_document_info('Encrypted', 'Yes')
        else:
            application_messages.print_document_info('Encrypted', 'No')

        if self.num_pages:
            application_messages.print_document_info('Pages', self.num_pages)

        if self.size:
            application_messages.print_document_info(
                'Size', self.size + ' bytes')
        print