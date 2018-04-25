import unittest

from homework_lesson2.homework_lesson1 import *

class TestCaseHomeWork1(unittest.TestCase):

    def test_random_list(self):
        pass

    def test_min_number(self):
        a = [35, 25, 10, 20]
        res = min_number(a)
        self.assertEqual(res, 10)

    def test_max_number(self):
        a = [10, 20, 5, 1]
        res = max(a)
        self.assertEqual(res, 20)

class TestCaseHomeWork2(unittest.TestCase):

    def test_random_list(self):
        pass

    def test_sort_ar(self):
        a = [8, 2, 1, 4]
        res = sort_ar(a)
        self.assertEqual(res, [1, 2, 4, 8])

    def test_insertion_sort(self):
        a = [3, 1, 5, 2]
        res = insertion_sort(a)
        self.assertEqual(res, [1, 2, 3, 5])

if __name__ == '__main__':
    import doctest

    doctest.testmod()