from sys import version_info
from types import FrameType

from presentation.messages.condition_messages import print_info


def get_interpreter_version() -> str:
    major, minor, micro, release, serial = version_info

    return major


# noinspection PyUnusedLocal
def handle_sigint(signal: int, frame: FrameType) -> None:
    print_info('Stopped')
    exit(0)
