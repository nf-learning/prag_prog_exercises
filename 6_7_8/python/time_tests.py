import unittest
from timeRegex import minutesAfterMidnight
class TestTimeConversion(unittest.TestCase):

    def test_valid_time_formats(self):
        self.assertEqual(minutesAfterMidnight('4pm'), 960)
        self.assertEqual(minutesAfterMidnight('7:38pm'), 1178)
        self.assertEqual(minutesAfterMidnight('23:42'), 1422)
        self.assertEqual(minutesAfterMidnight('3:16'), 196)
        self.assertEqual(minutesAfterMidnight('3:16am'), 196)
        self.assertEqual(minutesAfterMidnight('12:00pm'), 720)
        self.assertEqual(minutesAfterMidnight('12:00am'), 0)

    def test_invalid_time_formats(self):
        self.assertIsNone(minutesAfterMidnight('abc'))
        self.assertIsNone(minutesAfterMidnight('12:99pm'))
        self.assertIsNone(minutesAfterMidnight('25:00'))
        self.assertIsNone(minutesAfterMidnight('am4'))
        self.assertIsNone(minutesAfterMidnight('pm12'))

if __name__ == '__main__':
    unittest.main()
