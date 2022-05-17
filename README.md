# pdfMetadata

	pdfMetadata is a python script that gets and displays metadata from
	pdf files.

REQUIREMENTS

    - PyPDF2

INSTALLATION

    Enter into the directory where is extracted pdfMetadata,
    e.g. ~/pdfMetadata, then runs:

    python setup.py install

USAGE

    pdfMetadata.py [-h] [--log <log file>] [--csv <csv file>]
                        TARGET [TARGET ...]

    -h, --help
        Display the help and exits.

    --log <log file>
        Saves the output to a text plain file.

    --csv <csv file>
        Saves the output to a csv file.

    TARGET
        Pdf files or directories to be scanned. They can be mixed. If
        TARGET is a directory, pdfMetadata scans it recursively
        searching pdf files to analyze.
        Ex:
            pdfMetadata foo.pdf /foo/bar bar.pdf
            
## Support
If you find this application useful you can star this repo.
