import unittest
from bubble_sort import bubble_sort

class armstrong_test(unittest.TestCase):
    '''Test that the output is a list'''
    def test_returns_list_type(self):
        self.assertEqual(type(bubble_sort([4, 3, 5, 0, 1])), list )
    def test_returns_sorted(self):
        self.assertEqual(bubble_sort([4, 3, 5, 0, 1]), [0, 1, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()