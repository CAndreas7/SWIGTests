import unittest
import divide

class TestDividePy(unittest.TestCase):

    def test_dividePy(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(-10, -2), 5)
        self.assertIsNone(divide(10, 0))

class TestDivideC(unittest.TestCase):

    def test_divideC(self):
        self.assertEqual(divide.divideC(10, 2), 5)
        self.assertEqual(divide.divideC(-10, 2), -5)
        self.assertEqual(divide.divideC(10, -2), -5)
        self.assertEqual(divide.divideC(-10, -2), 5)
        self.assertIsNone(divide.divideC(10, 0))

if __name__ == '__main__':
    unittest.main()
