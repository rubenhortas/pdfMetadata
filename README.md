# pdfMetadata

pdfMetadata is a python script that gets and displays metadata from
PDF files.

pdfMetadata can extract data from one PDF file or for all PDF files in a directory (scans recursively).

![GitHub repo file count](https://img.shields.io/github/directory-file-count/rubenhortas/pdfMetadata)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/rubenhortas/pdfMetadata)
![GitHub repo size](https://img.shields.io/github/repo-size/rubenhortas/pdfMetadata)

![GitHub issues](https://img.shields.io/github/issues-raw/rubenhortas/pdfMetadata?logo=github)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/rubenhortas/pdfMetadata?logo=github)
![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/rubenhortas/pdfMetadata?&logo=github)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed-raw/rubenhortas/pdfMetadata?logo=github)
![GitHub all releases](https://img.shields.io/github/downloads/rubenhortas/pdfMetadata/total?logo=github)

## REQUIREMENTS

* Python3
* PyPDF2
* colorama

## INSTALLATION

Enter into the directory where is extracted pdfMetadata, e.g. ~/pdfMetadata, then runs:

```shell
python setup.py install
```

## USAGE

```shell
usage: pdfMetadata [-h] [-t [log_file.txt]] [-c [log_file.csv]] [-a] ARGUMENTS [ARGUMENTS ...]

Scan pdf files looking for their metadata.

positional arguments:
  ARGUMENTS             file[s] or path[s] to scan pdf files

options:
  -h, --help            show this help message and exit
  -t [log_file.txt], --txt [log_file.txt]
                        Saves the output into a plain text file.
  -c [log_file.csv], --csv [log_file.csv]
                        Saves the output into a csv file.
  -a, --show-all        Shows scanned non-PDF files.
```

## Troubleshooting

In case of any problem create an [issue](https://github.com/rubenhortas/pdfMetadata/issues/new)

## Discussions

If you want ask (or answer) a question, leave an opinion or have an open-ended conversation you can create (or join)
a [discussion](https://github.com/rubenhortas/pdfMetadata/discussions/new)

## Support

If you find this application useful you can star this repo.
