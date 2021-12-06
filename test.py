import unittest
import mainn

arr = [1, 2, 4, 1, 3]
sum = 7

class Test(unittest.TestCase):
    def test_love(self):
        self.assertEqual(mainn.find_sum(arr, sum), True)