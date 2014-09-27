#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:  Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact: rubenhortas at gmail.com
@github:  http://github.com/rubenhortas
@license: CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:    pdfMetadata.py
"""

from PyPDF2 import PdfFileReader
import os
import data.Date as Date

from presentation import(Messages, MessagesMetadata)


class PDFMetadata:
    """
    Class PDFMetadata
        Stores the data and operations relatives to the pdf
        (metadata, pages, size...).
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

    def __init__(self, file_path):
        """
        __init__(self, file_path):
            - Try to open the pdf.
            - Get the metadata.
            - Print the metadata.
        Arguments:
            - file_path: (string) Absolute file path.
        """

        self.abs_path = file_path
        self.name = os.path.basename(self.abs_path)

        try:
            pdf_file = PdfFileReader(file(self.abs_path, 'rb'))
            self.encrypted = self.__is_encrypted(pdf_file)
            doc_info = pdf_file.getDocumentInfo()
            if doc_info:
                self.__parse_info(doc_info)
                self.__print_metadata()

        except Exception, e:
            if 'encode' not in str(e):
                Messages.error_msg(str(e))
                print

    def __is_encrypted(self, pdf_file):
        """
        __is_encrypted(self, pdf_file)
            Return if pdf_file is encrypted or not.
        Arguments:
            - pdf_file: (pdfFileReader) PDF file.
        """

        if pdf_file.getIsEncrypted():
            try:
                pdf_file.decrypt('')
            except Exception:
                pass
            finally:
                return 'Yes'
        else:
            return 'No'

    def __parse_info(self, doc_info):
        """
        __parse_info(self, doc_info)
            Parses the metadata.
        Arguments:
            - doc_info: (pdfFileReader.getDocumentInfo()) Metadata.
        """

        file_name = doc_info.get('/Title', None)
        if file_name:
            self.title = file_name.encode('utf-8')

        author = doc_info.get('/Author', None)
        if author:
            self.author = author.encode('utf-8')

        creator = doc_info.get('/Creator', None)
        if creator:
            self.creator = creator.encode('utf-8')

        subject = doc_info.subject
        if subject and (subject != ''):
            self.subject = subject.encode('utf-8')

        producer = doc_info.get('/Producer', None)
        if producer:
            if producer != '':
                producer = producer.strip()
                self.producer = producer.encode('utf-8')

        creation_date = doc_info.get('/CreationDate', None)
        if creation_date:
            self.creation_date = Date.format_date(creation_date)

        modification_date = doc_info.get('/ModDate', None)
        if modification_date:
            self.modification_date = Date.format_date(modification_date)

    def __print_metadata(self):
        """
        __print_metadata(self)
            Displays the metadata in a nice format.
        """

        MessagesMetadata.file_name(self.name)
        MessagesMetadata.info('Path', self.abs_path)

        if self.title:
            MessagesMetadata.info('Title', self.title)

        if self.author:
            MessagesMetadata.highlighted('Author', self.author)

        if self.creator:
            MessagesMetadata.info('Creator', self.creator)

        if self.subject:
            MessagesMetadata.info('Subject', self.subject)

        if self.producer:
            MessagesMetadata.info('Producer', self.producer)

        if self.creation_date:
            MessagesMetadata.info_date('Creation date', self.creation_date)

        if self.modification_date:
            MessagesMetadata.info_date('Modification date',
                                       self.modification_date)

        MessagesMetadata.info('Encrypted', self.encrypted)

        if self.num_pages:
            MessagesMetadata.info('Pages', self.num_pages)

        if self.size:
            MessagesMetadata.info('Size', self.size + ' bytes')

        print
