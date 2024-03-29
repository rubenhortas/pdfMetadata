from crosscutting.condition_messages import print_exception
from log import Log


class LogCsv(Log):
    def __init__(self, name):
        super(LogCsv, self).__init__(name, '.csv', ',')

        self.__write_header()

    def __write_header(self):
        """
        __write_header(self)
            Writes CSV file header.
        """

        try:
            f_log = open(self.file_name, 'w')
            f_log.write('#File name, Path, Title, Author, Creator, Subject,'
                        ' Producer, Creation date, Modification date,'
                        ' Encrypted, Pages, Size, Keywords\n')
            f_log.close()
        except Exception as ex:
            print_exception(ex)

    def write(self, metadata):
        try:
            f_log = open(self.file_name, 'a+')
            if metadata.name:
                f_log.write(metadata.name)

            f_log.write(self.field_separator)

            if metadata.absolute_path:
                f_log.write(metadata.absolute_path)

            f_log.write(self.field_separator)

            if metadata.title:
                f_log.write(metadata.title)

            f_log.write(self.field_separator)

            if metadata.author:
                f_log.write(metadata.author)

            f_log.write(self.field_separator)

            if metadata.creator:
                f_log.write(metadata.creator)

            f_log.write(self.field_separator)

            if metadata.subject:
                f_log.write(metadata.subject)

            f_log.write(self.field_separator)

            if metadata.producer:
                f_log.write(metadata.producer)

            f_log.write(self.field_separator)

            if metadata.creation_date:
                f_log.write(metadata.creation_date)

            f_log.write(self.field_separator)

            if metadata.modification_date:
                f_log.write(metadata.modification_date)

            f_log.write(self.field_separator)

            f_log.write(metadata.encrypted)
            f_log.write(self.field_separator)

            if metadata.num_pages:
                f_log.write(metadata.num_pages)

            f_log.write(self.field_separator)

            if metadata.size:
                f_log.write(metadata.size)

            f_log.write(self.field_separator)

            if metadata.keywords:
                f_log.write(metadata.keywords)

            f_log.write('\n')
            f_log.close()

        except Exception as ex:
            print_exception(ex)
