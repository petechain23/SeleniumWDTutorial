import unittest

class TestClass1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("=\=" *30)
        print("TestClass1: setUpClass -> All Test in TestClass1 are starting")

    def setUp(self):
        print("TestClass1: setUp -> This step will run once before every test")

    def test_MethodA(self):
        print("TestClass1: Run method A")

    def test_MethodB(self):
        print("TestClass1: Run method B")

    def tearDown(self):
        print("TestClass1: tearDown -> This step will run after every test")

    @classmethod
    def tearDownClass(cls):
        print("TestClass1: tearDownClass -> All Test in TestClass1 are completed")
        print("=/=" * 30)

if __name__ == '__main__':
    unittest.main(verbosity=2)