from pathlib import Path

from PyPDF2 import PdfReader
from PyPDF2.errors import DependencyError

from domain.utils.date_utils import get_date


class Metadata:
    """
    Class Metadata
        Data and operations relatives to the PDF file.
    """

    file_abs_path: str = ""
    file_name: str = ""
    title: str = ""
    author: str = ""
    creator: str = ""
    subject: str | None = ""
    producer: str = ""
    creation_date: str = ""
    modification_date: str = ""
    encrypted: str = ""
    num_pages: str = ""
    size: str = ""
    keywords: str = ""

    def __init__(self, file: str) -> None:
        self.file_abs_path: str = file
        self.file_name: str = Path(file).name
        self.size = str(Path(file).stat().st_size)

        document = PdfReader(self.file_abs_path, False)

        try:
            self.encrypted = "Yes" if document.is_encrypted else "No"
            self.num_pages = str(len(document.pages))

            metadata = document.metadata

            if metadata is not None:
                self.title = metadata.get("/Title", "")
                self.keywords = metadata.get("/Keywords", "")
                self.author = metadata.get("/Author", "")
                self.creator = metadata.get("/Creator", "")
                self.producer = metadata.get("/Producer", "")
                self.creation_date = get_date(metadata.get("/CreationDate", ""))
                self.modification_date = get_date(metadata.get("/ModDate", ""))
                self.subject = getattr(metadata, "subject", "")
            else:
                self.title = ""
                self.keywords = ""
                self.author = ""
                self.creator = ""
                self.producer = ""
                self.creation_date = ""
                self.modification_date = ""
                self.subject = ""
        except DependencyError:
            pass

    def to_txt(self) -> str:
        def _get_field_value(name: str, attribute: object) -> None:
            if attribute:
                data.append(f"{name}: {attribute}")

        data = []

        _get_field_value("File", self.file_name)
        _get_field_value("Path", self.file_abs_path)
        _get_field_value("Title", self.title)
        _get_field_value("Author", self.author)
        _get_field_value("Creator", self.creator)
        _get_field_value("Subject", self.subject)
        _get_field_value("Producer", self.producer)
        _get_field_value("Creation date", self.creation_date)
        _get_field_value("Modification date", self.modification_date)
        _get_field_value("Encrypted", self.encrypted)
        _get_field_value("Pages", self.num_pages)
        _get_field_value("Size", self.size)
        _get_field_value("Keywords", self.keywords)

        data.append("\n")

        return "\n".join(data)

    def to_csv(self) -> str:
        def _get_field_value(attribute: object) -> None:
            if attribute:
                data.append(str(attribute))
            else:
                data.append("")

        # Header: File, Path, Title, Author, Creator, Subject, Producer, Creation date, Modification date, Encrypted,
        # Pages, Size, Keywords
        data = []

        _get_field_value(self.file_name)
        _get_field_value(self.file_abs_path)
        _get_field_value(self.title)
        _get_field_value(self.author)
        _get_field_value(self.creator)
        _get_field_value(self.subject)
        _get_field_value(self.producer)
        _get_field_value(self.creation_date)
        _get_field_value(self.modification_date)
        _get_field_value(self.encrypted)
        _get_field_value(self.num_pages)
        _get_field_value(self.size)
        _get_field_value(self.keywords)

        data.append("\n")

        return ",".join(data)
