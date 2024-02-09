import unittest
from divide.divide import dividePy


class TestUnittest(unittest.TestCase):

    def test_unittest_dividePy(self):
        self.assertEqual(dividePy(10, 2), 5)
        self.assertEqual(dividePy(-10, 2), -5)
        self.assertEqual(dividePy(10, -2), -5)
        self.assertEqual(dividePy(-10, -2), 5)
        self.assertIsNone(dividePy(10, 0))

if __name__ == '__main__':
    unittest.main()
