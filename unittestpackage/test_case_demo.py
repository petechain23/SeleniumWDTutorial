import unittest

class TestCaseDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("=\=" *30)
        print("setUpClass -> Run only once before all tests")

    def setUp(self):
        print("setUp -> This step will run once before every test")

    def test_MethodA(self):
        print("Run method A")

    def test_MethodB(self):
        print("Run method B")

    def tearDown(self):
        print("tearDown -> This step will run after every test")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass -> Run only once after all tests")
        print("=/=" * 30)

if __name__ == '__main__':
    unittest.main(verbosity=2)