from sys import version_info
from crosscutting.condition_messages import print_info


def get_interpreter_version():
    major, minor, micro, release, serial = version_info

    return major


# noinspection PyUnusedLocal
def handle_sigint(signal, frame):
    print_info('Stopped')
    exit(0)
