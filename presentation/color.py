class Color:
    """
    Class color
        Colors the text to display it in the output.
    """

    bold = '\033[1m'

    green = '\033[32m'
    red = '\033[31m'
    orange = '\033[93m'
    yellow = '\033[33m'

    bold_green = bold + green
    bold_red = bold + red
    bold_orange = bold + orange
    bold_yellow = bold + yellow

    end = '\033[0m'
