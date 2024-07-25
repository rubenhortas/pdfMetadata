from presentation.messages.tag import Tag


def print_error(msg: str) -> None:
    print(f"{Tag.error} {msg}")


def print_info(msg: str) -> None:
    print(msg)


def print_exception(msg: str) -> None:
    print(f"{Tag.exception} {msg}")
