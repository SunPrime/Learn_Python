import unittest

from for_test.test.f1_test import ExpectedFailureTestCase

suite = unittest.TestLoader().loadTestsFromTestCase(ExpectedFailureTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)