from bubble_sort import bubble_sort
import unittest


class BubbleSort(unittest.TestCase):

    def test_for_functionality1(self):
        self.assertEqual(bubble_sort([0,4,2,3,5]), [0,2,3,4,5])

    def test_for_functionality2(self):
        self.assertEqual(bubble_sort([5,4,2,2,5]), [2,2,4,5,5])

    def test_for_functionality3(self):
        self.assertEqual(bubble_sort([8,4,3,7,2]), [2,3,4,7,8])
    
if __name__ == '__main__':
    unittest.main()