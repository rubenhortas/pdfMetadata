import re
from datetime import datetime

_FORMAT_1 = re.compile(r'^D:\d{14}')  # Formats: D:20071123033349Z, D:20080219165253+01'00
_FORMAT_2 = re.compile(r'\d{1,2}/\d{1,2}/\d{4} \d{2}:\d{2}:\d{2}')  # Format: 3/22/2004 18:21:23
_FORMAT_3 = re.compile(r'^([a-z]{3} ){2}\d{2} (\d{2}:){2}\d{2} \d{4}',
                       re.IGNORECASE)  # Format:  Mon Mar 14 13:55:36 2005


def get_date(date: str) -> str:
    """
    get_date(date)
        Formats a date.

    :param date: input date
    :return: string formatted date
    """
    if _FORMAT_1.match(date):
        date_format1 = _FORMAT_1.match(date).group(0)
        d = datetime.strptime(date_format1, 'D:%Y%m%d%H%M%S')
        return d.strftime('%H:%M:%S %d/%b/%Y (%a)')

    if _FORMAT_2.match(date):
        d = datetime.strptime(date, '%m/%d/%Y %H:%M:%S')
        return d.strftime('%H:%M:%S %d/%b/%Y (%a)')

    if _FORMAT_3.match(date):
        d = datetime.strptime(date, '%a %b %d %H:%M:%S %Y')
        return d.strftime('%H:%M:%S %d/%b/%Y (%a)')

    return date
