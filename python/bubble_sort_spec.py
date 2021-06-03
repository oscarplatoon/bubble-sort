from bubble_sort import bubble_sort
import unittest

class TestStringMethods(unittest.TestCase):

    def test_same(self):
        output = bubble_sort([4,3,5,0,1])
        self.assertEqual(output, [0,1,3,4,5])

    def test_same_same(self):
        output = bubble_sort([4,10,5,4,11])
        self.assertEqual(output, [4,4,5,10,11])
    
    def test_same_another(self):
        output = bubble_sort([41,13,51,0,31])
        self.assertEqual(output, [0,13,31,41,51])
    
    def test_another_another(self):
        output = bubble_sort([14,31,15,10,1])
        self.assertEqual(output, [1,10,14,15,31])

if __name__ == '__main__':
    unittest.main()
