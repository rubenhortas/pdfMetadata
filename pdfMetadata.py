import argparse
import signal

from application.pdf_metadata import get_metadata
from crosscutting.utils.python_utils import handle_sigint
from crosscutting.utils.python_utils import get_interpreter_version
from domain.metadata import Metadata
from presentation.cli import print_metadata
from presentation.messages.condition_messages import print_error, print_info
from crosscutting.constants import REQUIRED_PYTHON_VERSION
from domain.log_csv import LogCsv
from domain.log_txt import LogTxt
from presentation.utils.screen import clear_screen

if __name__ == '__main__':
    signal.signal(signal.SIGINT, handle_sigint)

    clear_screen()

    interpreter_version = get_interpreter_version()

    if interpreter_version == REQUIRED_PYTHON_VERSION:
        parser = argparse.ArgumentParser(prog='pdfMetadata', description='Scan pdf files looking for their metadata.')
        parser.add_argument('arguments', metavar='ARGUMENTS', nargs='+', help='file[s] or path[s] to scan pdf files')
        parser.add_argument('--log', metavar='log file', nargs='?', help='Saves the output into a plain text file.')
        parser.add_argument('--csv', metavar='csv file', nargs='?', help='Saves the output into a csv file.')
        args = parser.parse_args()

        if args.log:
            log_txt = LogTxt(args.log)

        if args.csv:
            log_csv = LogCsv(args.csv)

        files_metadata = []

        for argument in args.arguments:
            print_info(f"Scanning {argument}...")
            files_metadata.extend(get_metadata(argument))

        if files_metadata:
            # TODO: logs
            file_metadata: Metadata
            for file_metadata in files_metadata:
                print_metadata(file_metadata)

        print_info('Done')
    else:
        print_error('Requires Python {0}'.format(REQUIRED_PYTHON_VERSION))
        exit(0)
