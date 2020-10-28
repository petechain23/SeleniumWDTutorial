# import packages
import unittest
from unittestpackage.test_class1 import TestClass1
from unittestpackage.test_class2 import TestClass2

# load all test_class
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestClass2)

# create a test suite combining tc1, tc2
test_suite = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(test_suite)