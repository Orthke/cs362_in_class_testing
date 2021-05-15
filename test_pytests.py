from palindrome import *
from word_count import *
import pytest

def test_palindromes():
    assert is_palindrome("anna") == True
    assert is_palindrome("AnNA") == True
    assert is_palindrome("peanut") == False

def test_palindromes_fail():
    assert is_palindrome("amazon") == True

def test_counts():
    assert count_words("The dog is brown") == 4
    assert count_words("") == 0
    assert count_words("Word") == 1

def test_counts_fail():
    assert count_words("The dog is brown") == 8