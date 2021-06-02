import unittest
import random
from bubble_sort import bubble_sort

class BubbleSortTestCase(unittest.TestCase):

    def test_one(self):
        sorted = bubble_sort([1,0,2,3,4,5])
        self.assertEqual(sorted, [0,1,2,3,4,5])

    def test_rand(self):
        #create empty list to throw randint into
        array = []
        #throw 5 random int's into list
        for i in range(5):
            array.append(random.randint(0,20))
        #sort using bubble sort function
        bubble_sorted = bubble_sort(array)
        #sort using python sort method to check against
        array.sort()
        #assert equal
        self.assertEqual(bubble_sorted, array)