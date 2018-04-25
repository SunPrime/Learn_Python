import unittest

from homework_lesson2.test.homework_lesson1_test import *

FailTestSuite = unittest.TestSuite()
FailTestSuite.addTest(unittest.makeSuite(TestCaseHomeWork1))
FailTestSuite.addTest(unittest.makeSuite(TestCaseHomeWork2))
print("count of tests: " + str(FailTestSuite.countTestCases()) + "\n")

runner = unittest.TextTestRunner(verbosity=2)
runner.run(FailTestSuite)