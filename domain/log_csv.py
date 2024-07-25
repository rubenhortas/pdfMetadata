from domain.log import Log
from domain.metadata import Metadata
from presentation.messages.condition_messages import print_exception


class LogCsv(Log):
    extension: str = 'csv'
    _delimiter: str = ','

    def __init__(self, file_name: str) -> None:
        super(LogCsv, self).__init__(file_name)

        self._write_header()

    def _write_header(self) -> None:
        try:
            f_log = open(self.file_name, 'w')
            f_log.write('#File name, Path, Title, Author, Creator, Subject,'
                        ' Producer, Creation date, Modification date,'
                        ' Encrypted, Pages, Size, Keywords\n')
            f_log.close()
        except Exception as e:
            print_exception(str(e))

    def write(self, metadata: Metadata) -> None:
        try:
            f_log = open(self.file_name, 'a+')
            if metadata.file_name:
                f_log.write(metadata.file_name)

            f_log.write(self._delimiter)

            if metadata.file_abs_path:
                f_log.write(metadata.file_abs_path)

            f_log.write(self._delimiter)

            if metadata.title:
                f_log.write(metadata.title)

            f_log.write(self._delimiter)

            if metadata.author:
                f_log.write(metadata.author)

            f_log.write(self._delimiter)

            if metadata.creator:
                f_log.write(metadata.creator)

            f_log.write(self._delimiter)

            if metadata.subject:
                f_log.write(metadata.subject)

            f_log.write(self._delimiter)

            if metadata.producer:
                f_log.write(metadata.producer)

            f_log.write(self._delimiter)

            if metadata.creation_date:
                f_log.write(metadata.creation_date)

            f_log.write(self._delimiter)

            if metadata.modification_date:
                f_log.write(metadata.modification_date)

            f_log.write(self._delimiter)

            f_log.write(metadata.encrypted)
            f_log.write(self._delimiter)

            if metadata.num_pages:
                f_log.write(metadata.num_pages)

            f_log.write(self._delimiter)

            if metadata.size:
                f_log.write(metadata.size)

            f_log.write(self._delimiter)

            if metadata.keywords:
                f_log.write(metadata.keywords)

            f_log.write('\n')
            f_log.close()

        except Exception as e:
            print_exception(str(e))
