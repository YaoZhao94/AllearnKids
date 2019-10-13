import unittest
import time_zone
import table

class TestStringMethods(unittest.TestCase):

    def time_zone_test(self):
        gmt_time = 'Tue, 24 Sep 2019 02:13:27 GMT'
        aest_time = 'Tue, 24 Sep 2019 12:13:27 AEST'
        self.assertEqual(time_zone.zone_change(gmt_time), aest_time)

    def recall_number_test(self):
        self.assertEqual(len(table.recall_table()),10)


if __name__ == '__main__':
    unittest.main()