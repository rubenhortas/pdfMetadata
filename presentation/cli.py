from colorama import Style, Fore

from domain.metadata import Metadata
from presentation.messages.tag import Tag


def print_metadata(metadata: Metadata) -> None:
    """
     print_metadata(metadata: Metadata)
        Prints the metadata in a nice format.
    """
    try:
        _print_file_name(metadata.file_name)
        _print_field('Path', metadata.file_abs_path)
        _print_field('Title', metadata.title)
        _print_field_highlighted('Author', metadata.author)
        _print_field('Creator', metadata.creator)
        _print_field('Subject', metadata.subject)
        _print_field('Producer', metadata.producer)
        _print_field('Creation date', metadata.creation_date)
        _print_field('Modification date', metadata.modification_date)

        if metadata.encrypted == 'Yes':
            _print_field_highlighted('Encrypted', metadata.encrypted)
        else:
            _print_field('Encrypted', metadata.encrypted)

        _print_field('Pages', metadata.num_pages)
        _print_field('Size', '{0} bytes'.format(metadata.size))
        _print_field('Keywords', metadata.keywords)

        print()
    except Exception as e:
        pass


def _print_file_name(name: str) -> None:
    print(f"{Tag.info}{Style.BRIGHT}{Fore.GREEN}{name}{Style.RESET_ALL}")


def _print_field(name: str, value: str) -> None:
    print(f"{Tag.info}{name}: {value}")


def _print_field_highlighted(name: str, value: str) -> None:
        print(
            f"{Tag.info}{Style.BRIGHT}{Fore.GREEN}{name}{Style.RESET_ALL}: {Style.BRIGHT}{Fore.RED}{value}{Style.RESET_ALL}")
