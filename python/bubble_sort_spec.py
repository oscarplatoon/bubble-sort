import unittest
from bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):

    """
    when you call bubble sort, you get a list back:
    """
    def test_returns_a_list(self):
        self.assertTrue(type(bubble_sort([1])) is list)

if __name__ == '__main__':
    unittest.main()