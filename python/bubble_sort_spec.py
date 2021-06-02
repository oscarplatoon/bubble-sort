import unittest
from bubble_sort import bubble_sort


test_list = [4,3,5,0,1]

class TestBubbleSort(unittest.TestCase):
  
    """
    when you call bubble sort, you get a list back:
    """
    def test_returns_a_list(self):
        self.assertTrue(type(bubble_sort([1])) is list)

    """
    Bubble Sort correctly sorts lists of integers:
    """
    def test_sort_accuracy(self):
        self.assertTrue(bubble_sort(test_list) == ([0,1,3,4,5]))

if __name__ == '__main__':
    unittest.main()