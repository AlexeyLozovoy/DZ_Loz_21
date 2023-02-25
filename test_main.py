import unittest
import main

class TestIntSet(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4, 5]
        self.intset = main.IntSet(self.data)

    def test_sum(self):
        self.assertEqual(self.intset.sum(), sum(self.data))

    def test_avg(self):
        self.assertEqual(self.intset.avg(), sum(self.data) / len(self.data))

    def test_max(self):
        self.assertEqual(self.intset.max(), max(self.data))

    def test_min(self):
        self.assertEqual(self.intset.min(), min(self.data))