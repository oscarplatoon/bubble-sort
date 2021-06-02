import unittest
from bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
  
    """
    when you call bubble sort, you get a ([sorted_list], swaps) tuple back:
    """
    def test_returns_a_list(self):
        self.assertTrue(type(bubble_sort([4, 3, 5, 0, 1])) == tuple)

    """
    Bubble Sort correctly sorts lists of integers:
    """
    def test_sort_accuracy(self):
        self.assertTrue(bubble_sort([4, 3, 5, 0, 1])[0] == ([0, 1, 3, 4, 5]))

    """
    The worst case for bubble sort is when the list is reverse ordered. 15 steps are required.
    """
    def test_worst_case(self):
        self.assertTrue(bubble_sort([5,4,3,2,1, 0]) == ([0,1,2,3,4,5], 15))

if __name__ == '__main__':
    unittest.main()
