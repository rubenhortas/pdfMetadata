from functools import wraps
from typing import Callable


def write_file(func: Callable) -> Callable:
    """
    Decorator to handle file writing when using the CLI interface.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError as file_not_found_error:
            print(f"'{file_not_found_error.filename}' no such file or directory")
        except PermissionError:
            # print(f"Permission denied: '{args.txt}'")
            print(f"Permission denied: ")
        except OSError as os_error:
            # print(f"'{args.txt}' OSError: {os_error}")
            print(f"OSError: {os_error}")

    return wrapper
