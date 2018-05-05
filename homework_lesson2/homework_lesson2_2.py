import unittest
def func_sqrt_test(func4test):
    def testtest(x, y):
        class Failfunc_sqrt_test(unittest.TestCase):
            def test_func4test(self):
                self.assertEqual(func4test(x, y), x ** y)

        suite = unittest.TestLoader().loadTestsFromTestCase(Failfunc_sqrt_test)
        unittest.TextTestRunner(verbosity=2).run(suite)
        return func4test(x, y)
    return testtest

@func_sqrt_test
def func_sqrt(a, b):
    return a ** b


num1 = 25
num2 = 3
res = func_sqrt(num1, num2)
print(res)
