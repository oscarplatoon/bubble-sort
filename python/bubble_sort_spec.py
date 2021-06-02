import unittest
from bubble_sort import bubble_sort

class bubbleSortTestCase(unittest.TestCase):
    """Tests for bubble_sort.py"""
    
    def test_1(self):
        self.assertEqual(bubble_sort([19, 13, 6, 2, 18, 8]), '[2, 6, 8, 13, 18, 19]')
        
    def test_2(self):
       self.assertEqual(bubble_sort([1, 2, 3, 4, 5, 6]), '[1, 2, 3, 4, 5, 6]')
    
    def test_3(self):
       self.assertNotEqual(bubble_sort([6, 5, 4, 3, 2, 1]), '[1, 2, 3, 4, 5, 6]')
        
    def test_4(self):
        self.assertNotEqual(bubble_sort([19, 13, 6, 2, 18, 8]), '[2, 6, 8, 13, 18, 19]')
        
if __name__ == '__main__':
    unittest.main() 