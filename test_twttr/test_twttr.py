import pytest
from twttr import shorten

def test_lowercase():
    assert shorten("hello") == "hll"

def test_uppercase():
    assert shorten("HELLO") == "HLL"

def test_mixed_case():
    assert shorten("TwItTeR") == "TwtTR"  # Fixed expected output

def test_no_vowels():
    assert shorten("bcdfgh") == "bcdfgh"

def test_all_vowels():
    assert shorten("aeiouAEIOU") == ""
import pytest
from twttr import shorten

def test_lowercase():
    assert shorten("hello") == "hll"

def test_uppercase():
    assert shorten("HELLO") == "HLL"

def test_mixed_case():
    assert shorten("TwItTeR") == "TwtTR"  # Fixed expected output

def test_no_vowels():
    assert shorten("bcdfgh") == "bcdfgh"

def test_all_vowels():
    assert shorten("aeiouAEIOU") == ""

def test_empty_string():
    assert shorten("") == ""

def test_single_char():
    assert shorten("a") == ""
    assert shorten("A") == ""
    assert shorten("b") == "b"
    assert shorten("B") == "B"

def test_with_numbers_and_punctuation():
    # Numbers and punctuation should be preserved
    assert shorten("hello123!") == "hll123!"
    assert shorten("aei9u,.") == "9,."
    assert shorten("1234!!") == "1234!!"

def test_empty_string():
    assert shorten("") == ""

def test_single_char():
    assert shorten("a") == ""
    assert shorten("A") == ""
    assert shorten("b") == "b"
    assert shorten("B") == "B"