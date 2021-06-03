import unittest
from bubble_sort import bubble_sort

class bubbleSortTest(unittest.TestCase):

  def test_return_sorted_(self):
    self.assertEqual(bubble_sort([2, 9, 4, 6, 1]), ([1, 2, 4, 6, 9], 6))
    self.assertEqual(bubble_sort([2, 9, 4, 6, 1, 0, 2]), ([0, 1, 2, 2, 4, 6, 9], 14))
    self.assertEqual(bubble_sort([2, 9, 4, 6, 1, 9, 1]), ([1, 1, 2, 4, 6, 9, 9], 11))

if __name__ == '__main__':
  unittest.main()