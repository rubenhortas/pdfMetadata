import argparse
import signal

from application.pdfMetadata_service import get_files, get_metadata
from crosscutting.constants import REQUIRED_PYTHON_VERSION
from crosscutting.utils.python_utils import get_interpreter_version
from crosscutting.utils.python_utils import handle_sigint
from presentation.cli import print_metadata, write_log_txt
from presentation.messages.condition_messages import print_error, print_info, print_exception
from presentation.utils.screen import clear_screen

if __name__ == '__main__':
    signal.signal(signal.SIGINT, handle_sigint)
    clear_screen()

    if get_interpreter_version() == REQUIRED_PYTHON_VERSION:
        parser = argparse.ArgumentParser(prog='pdfMetadata', description='Scan pdf files looking for their metadata.')
        parser.add_argument('arguments', metavar='ARGUMENTS', nargs='+', help='file[s] or path[s] to scan pdf files')
        parser.add_argument('-t', '--txt', metavar='log_file.txt', nargs='?',
                            help='Saves the output into a plain text file.')
        parser.add_argument('-c', '--csv', metavar='log_file.csv', nargs='?', help='Saves the output into a csv file.')
        parser.add_argument('-a', '--show-all', default=False, action='store_true',
                            help='Shows scanned non-PDF files..')
        args = parser.parse_args()

        try:
            print_info('\nGetting PDF files...')
            pdf_files, non_pdf_files = get_files(args.arguments)

            print_info('Getting metadata from PDF files...')
            pdf_files_metadata, pdf_files_errors = get_metadata(pdf_files)

            print_info('Metadata:\n')
            for file_metadata in pdf_files_metadata:
                print_metadata(file_metadata)

            if args.txt:
                write_log_txt(args.txt, pdf_files_metadata)

            if args.csv:
                write_log_txt(args.csv, pdf_files_metadata)

            if pdf_files_errors:
                print('PDFs not scanned: ', end='')
                print(', '.join(pdf_files_errors))

            if args.show_all and non_pdf_files:
                print('Regular files not scanned: ', end='')
                print(', '.join(non_pdf_files))

            pdf_num = len(pdf_files)
            total_files = pdf_num + len(non_pdf_files)

            print_info(f"PDFs found: {pdf_num}/{total_files} files")
            print_info(f"PDFs processed: {pdf_num - len(pdf_files_errors)}/{pdf_num}")
            print_info('Done')
        except Exception as e:
            print_exception(str(e))
    else:
        print_error('Requires Python {0}'.format(REQUIRED_PYTHON_VERSION))
        exit(0)
