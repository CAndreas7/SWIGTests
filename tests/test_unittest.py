import unittest
from divide import dividePy
from main import add, multiply
from unittest.mock import patch


class TestUnittest(unittest.TestCase):

    def test_unittest_dividePy(self):
        self.assertEqual(dividePy(10, 2), 5)
        self.assertEqual(dividePy(-10, 2), -5)
        self.assertEqual(dividePy(10, -2), -5)
        self.assertEqual(dividePy(-10, -2), 5)
        self.assertIsNone(dividePy(10, 0))
        
    def test_add(self):
        with patch('main.add', return_value=10):
            result = add(3, 7)
            self.assertEqual(result, 10)

    def test_multiply(self):
        with patch('main.add', return_value=15):
            result = multiply(3, 5)
            self.assertEqual(result, 15)

if __name__ == '__main__':
    unittest.main()