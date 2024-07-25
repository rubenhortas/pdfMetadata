import unittest

from domain.utils.date_utils import get_date


class DateTest(unittest.TestCase):
    def setUp(self):
        self.dates = [
            ('D:20071123033349Z', '03:33:49 23/Nov/2007 (Fri)'),
            ('D:20080219165253+01\'00', '16:52:53 19/Feb/2008 (Tue)'),
            ('3/22/2004 18:21:23', '18:21:23 22/Mar/2004 (Mon)'),
            ('Mon Mar 14 13:55:36 2005', '13:55:36 14/Mar/2005 (Mon)'),
            ('13:55:36 14/Mar/2005 (Mon)', '13:55:36 14/Mar/2005 (Mon)'),
            (None, None)
        ]

    def test_date_format(self):
        for date, expected_result in self.dates:
            self.assertEqual(expected_result, get_date(date))
