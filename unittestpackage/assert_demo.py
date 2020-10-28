import unittest

class AssertDemo(unittest.TestCase):
    def test_AssertTrueFalse(self):
        a = True
        self.assertTrue(a, "a is not true")
        b = False
        self.assertFalse(b, "b is not false")

    def test_AssertEqual(self):
        a = 'test'
        b = 'test'
        self.assertEqual(a, b, msg="a is not equal to b")

if __name__ == '__main__':
    unittest.main(verbosity=2)
