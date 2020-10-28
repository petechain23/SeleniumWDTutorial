import unittest

class TestClass2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("=\=" *30)
        print("TestClass2: setUpClass -> All Test in TestClass2 are starting")

    def setUp(self):
        print("TestClass2: setUp -> This step will run once before every test")

    def test_MethodA(self):
        print("TestClass2: Run method A")

    def test_MethodB(self):
        print("TestClass2: Run method B")

    def tearDown(self):
        print("TestClass2: tearDown -> This step will run after every test")

    @classmethod
    def tearDownClass(cls):
        print("TestClass2: tearDownClass -> All Test in TestClass2 are completed")
        print("=/=" * 30)

if __name__ == '__main__':
    unittest.main(verbosity=2)