pdfMetadata
===========

	pdfMetadata is a python script that gets and displays metadata from
	pdf files.

AUTHOR

    Rubén Hortas
    Contact: rubenhortas at gmail.com
    Website: http://www.rubenhortas.blogspot.com.es

LICENSE

    CC BY-NC-SA 3.0
    http://creativecommons.org/licenses/by-nc-sa/3.0/

REQUIREMENTS

    PyPDF2

INSTALLATION

    Enter into the directory where is extracted pdfMetadta,
    f.e: ~/pdfMetadata, then runs:

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
            pdfMetdata foo.pdf /foo/bar bar.pdf


CONTACT

    If you have problems, questions, ideas or suggestions, you can
    contribute with this little project in the github repository

    https://github.com/rubenhortas/pdfMetadata

WEB SITE

    Visit the pdfMetadata github site for the lastest news and downloads:

    https://github.com/rubenhortas/pdfMetadata
