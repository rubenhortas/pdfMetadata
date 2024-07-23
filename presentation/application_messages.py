from presentation.tag import Tag
from colorama import Fore, Style


def print_file_name(name: str) -> None:
    print(f"{Tag.info}{Style.BRIGHT}{Fore.GREEN}{name}{Style.RESET_ALL}")


def print_field(name: str, value: str) -> None:
    print(f"{Tag.info}{name}:\t\t{value}")


def print_field_highlighted(name: str, value: str) -> None:
    print(
        f"{Tag.info}{Style.BRIGHT}{Fore.GREEN}{name}{Style.RESET_ALL}:\t\t{Style.BRIGHT}{Fore.RED}{value}{Style.RESET_ALL}")
