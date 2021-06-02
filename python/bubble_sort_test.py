import unittest
import random
from bubble_sort import bubble_sort

class BubbleSortTestCase(unittest.TestCase):

    def test_case_1(self):
        output = bubble_sort([1, 0, 2, 3, 4, 5])
        self.assertEqual(output, [0,1,2,3,4,5])

    def test_case_2(self):
        output = bubble_sort([1, 7, 3, 54, -1, 0])
        self.assertEqual(output, [-1,0,1,3,7,54])
    
    def test_case3(self):
        input = []
        for x in range(20):
            input.append(random.randint(0, 100))
        output = bubble_sort(input)
        input.sort()
        self.assertEqual(output, input)

if __name__ == '__main__':
    unittest.main()