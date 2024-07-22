import unittest

from application.utils.date_utils import get_date


class DateTest(unittest.TestCase):
    def setUp(self):
        self.date_format1_1 = 'D:20071123033349Z'
        self.date_format1_2 = 'D:20080219165253+01\'00'
        self.date_format2 = '3/22/2004 18:21:23'
        self.date_format3 = 'Mon Mar 14 13:55:36 2005'

    def test_date_format(self):
        self.assertEqual('03:33:49 23/Nov/2007 (Fri)', get_date(self.date_format1_1))
        self.assertEqual('16:52:53 19/Feb/2008 (Tue)', get_date(self.date_format1_2))
        self.assertEqual('18:21:23 22/Mar/2004 (Mon)', get_date(self.date_format2))
        self.assertEqual('13:55:36 14/Mar/2005 (Mon)', get_date(self.date_format3))
