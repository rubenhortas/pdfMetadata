import re
from datetime import datetime

_FORMAT_1 = re.compile('^D:[0-9]{14}')  # Formats: D:20071123033349Z, D:20080219165253+01'00
_FORMAT_2 = re.compile('[0-9]{1,2}/[0-9]{1,2}/[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2}')  # Format: 3/22/2004 18:21:23
_FORMAT_3 = re.compile('^[a-zA-Z]{3} [a-zA-Z]{3} [0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} [0-9]{4}')  # Format:  Mon Mar 14 13:55:36 2005


def get_date(date: str) -> str:
    """
    get_date(date)
        Converts the dates of metadata to a readable format.

    :param date: input date
    :return date_: date formatted as string
    """
    date_ = date

    if _FORMAT_1.match(date):
        date_format1 = _FORMAT_1.match(date).group(0)
        d = datetime.strptime(date_format1, 'D:%Y%m%d%H%M%S')
        date_ = d.strftime('%H:%M:%S %d/%b/%Y (%a)')

    if _FORMAT_2.match(date):
        d = datetime.strptime(date, '%m/%d/%Y %H:%M:%S')
        date_ = d.strftime('%H:%M:%S %d/%b/%Y (%a)')

    if _FORMAT_3.match(date):
        d = datetime.strptime(date, '%a %b %d %H:%M:%S %Y')
        date_ = d.strftime('%H:%M:%S %d/%b/%Y (%a)')

    return date_
