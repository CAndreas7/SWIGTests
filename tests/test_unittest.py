import unittest
from operations import *
from unittest.mock import patch


class TestUnittest(unittest.TestCase):

    def test_unittest_dividePy(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(-10, -2), 5)
        self.assertIsNone(divide(10, 0))
        
    def test_add(self):
        self.assertEqual(add(1,1), 2)
        self.assertEqual(add(2,1), 3)
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(-1,-1), -2)
        self.assertEqual(add(-1,1), 0)
            
    def test_subtract(self):
        self.assertEqual(subtract(1,1), 0)
        self.assertEqual(subtract(2,1), 1)
        self.assertEqual(subtract(1,2), -1)
        self.assertEqual(subtract(-1,-1), 0)
        self.assertEqual(subtract(-1,1), -2)
        
    def test_multiply(self):
        with patch('operations.add', return_value=15):
            result = multiply(3, 5)
            self.assertEqual(result, 15)
            