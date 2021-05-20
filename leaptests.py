from leapyear import *
import unittest

class TestStringMethods(unittest.TestCase):

    def test_actual(self):
        self.assertEqual(is_leap_year("1776"), True)

    def test_wrong(self):
        self.assertEqual(is_leap_year("2021"), False)

    def test_fail(self):
        self.assertEqual(is_leap_year("1999"), True)


if __name__ == "__main__":
    unittest.main()

