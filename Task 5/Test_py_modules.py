from Py_modules_T5 import *
import unittest
class Test_Python_Module(unittest.TestCase):
    def test_Is_vowels_in_the_string(self):
        self.assertTrue([]!=vowels("Hello i am here"))
    def test_not_vowels_in_the_string(self):
        self.assertTrue([]==vowels("gftrhklpbxzw"))
    def test_have_factors(self):
        self.assertTrue([]!=factors(5))
    def test_have_not_factors(self):
        self.assertTrue([]==factors(3))
    def test_is_prime(self):
        self.assertTrue(True==is_prime(89))
    def test_is_not_prime(self):
        self.assertFalse(True==is_prime(4))
    def test_len(self):
        self.assertTrue(14   ==len("This is a exam"))
    


if __name__=="__main__":
    unittest.main()
