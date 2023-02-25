import unittest
from utils.arrs import get, my_slice


class TestGet(unittest.TestCase):

    def test_positive_index(self):
        self.assertEqual(get([1, 2, 3, 4], 2), 3)

    def test_negative_index(self):
        self.assertEqual(get([1, 2, 3, 4], -1), None)


class TestMy_slice(unittest.TestCase):

    def test_slice(self):
        self.assertEqual(my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(my_slice([1, 2, 3], 1), [2, 3])

    def test_slice_3(self):
        self.assertEqual(my_slice([]), [])

    def test_slice_4(self):
        self.assertEqual(my_slice([1, 2, 3, 4], -1), [4])

    def test_slice_5(self):
        self.assertEqual(my_slice([1, 2, 3], -5), [1, 2, 3])