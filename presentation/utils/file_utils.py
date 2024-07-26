from functools import wraps
from typing import Callable

from presentation.messages.condition_messages import print_error


def write_file(func: Callable) -> Callable:
    """
    Decorator to handle file writing when using the CLI interface.
    """

    @wraps(func)
    def wrapper(file: str, lines: list):
        try:
            return func(file, lines)
        except FileNotFoundError as file_not_found_error:
            print_error(f"'{file_not_found_error.filename}' no such file or directory")
        except PermissionError:
            print_error(f"Permission denied: '{file}'")
        except OSError as os_error:
            print_error(f"'{file}' OSError: {os_error}")

    return wrapper
