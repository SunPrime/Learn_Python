import unittest
from for_test.f1 import sum1

class ExpectedFailureTestCase(unittest.TestCase):
    def test_sum1(self):
       a = 10
       b = 20
       res = sum1(10, 20)
       self.assertEqual(res, 30)

if __name__ == '__main__':
    unittest.main()