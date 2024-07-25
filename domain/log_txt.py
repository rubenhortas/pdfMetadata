from domain.log import Log
from domain.metadata import Metadata
from presentation.messages.condition_messages import print_exception


class LogTxt(Log):
    extension = 'txt'

    def __init__(self, file_name: str) -> None:
        super(LogTxt, self).__init__(file_name)

    def write(self, metadata: Metadata) -> None:
        try:
            f_log = open(self.file_name, 'a+')
            if metadata.file_name:
                f_log.write('File: {0}\n'.format(metadata.file_name))

            if metadata.file_abs_path:
                f_log.write('Path: {0}\n'.format(metadata.file_abs_path))

            if metadata.title:
                f_log.write('Title: {0}\n'.format(metadata.title))

            if metadata.author:
                f_log.write('Author: {0}\n'.format(metadata.author))

            if metadata.creator:
                f_log.write('Creator: {0}\n'.format(metadata.creator))

            if metadata.subject:
                f_log.write('Subject: {0}\n'.format(metadata.subject))

            if metadata.producer:
                f_log.write('Producer: {0}\n'.format(metadata.producer))

            if metadata.creation_date:
                f_log.write('Creation date: {0}\n'.format(metadata.creation_date))

            if metadata.modification_date:
                f_log.write('Modification date: {0}\n'.format(metadata.modification_date))

            f_log.write('Encrypted: {0}\n'.format(metadata.encrypted))

            if metadata.num_pages:
                f_log.write('Pages: {0}\n'.format(metadata.num_pages))

            if metadata.size:
                f_log.write('Size: {0}\n'.format(metadata.size))

            if metadata.keywords:
                f_log.write('Keywords: {0}\n'.format(metadata.keywords))

            f_log.write('\n')
            f_log.close()
        except Exception as e:
            print_exception(str(e))
