from presentation.tag import Tag


def print_error(msg: str) -> None:
    print('{0}{1}\n'.format(Tag.error, msg))


def print_info(msg: str) -> None:
    print('{0}{1}'.format(Tag.info, msg))


def print_exception(msg: str) -> None:
    print('{0}{1}\n'.format(Tag.exception, msg))
