from palindrome import *
from word_count import *
import unittest
import pytest


class TestStringMethods(unittest.TestCase):

    def test_actual(self):
        self.assertEqual(is_palindrome("tacocat"), True)

    def test_capitals(self):
        self.assertEqual(is_palindrome("AnNA"), True)

    def test_fail(self):
        self.assertEqual(is_palindrome("amazon"), True)

    def test_non(self):
        self.assertEqual(is_palindrome("peanut"), False)

    def test_wc(self):
        self.assertEqual(count_words("The color is blue"), 4)
    
    def test_single(self):
        self.assertEqual(count_words("Word"), 1)

    def test_none(self):
        self.assertEqual(count_words(""), 0)

    def test_fail(self):
        self.assertEqual(count_words("This is my sentence"), 10)


if __name__ == "__main__":
    unittest.main()

