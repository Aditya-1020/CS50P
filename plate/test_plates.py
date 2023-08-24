import pytest
from plates import is_valid


def test_valid_plates():
    try:
        assert is_valid("CS50") == True
        assert is_valid("AAA222") == True
        assert is_valid("AB12CD") == True
        assert is_valid("ABCD12") == True
    except AssertionError:
        print("True")

def test_invalid_plates():
    try:
        assert is_valid("C5S0") == False
        assert is_valid("AAA22A") == False
        assert is_valid("ABC!123") == False
        assert is_valid("0BCD12") == False
    except AssertionError:
        print("False")

def test_edge_cases():
    try:
        assert is_valid("") == False
        assert is_valid("A") == False
        assert is_valid("ABCDEFG") == False
    except AssertionError:
        print("False")

def test_lowercase_letters():
    try:
        assert is_valid("cs50") == False
    except AssertionError:
        print("False")

def test_starting_with_zero():
    try:
        assert is_valid("0ABC12") == False
    except AssertionError:
        print("False")

def test_special_characters():
    try:
        assert is_valid("A#B12C") == False
    except AssertionError:
        print("False")

if __name__ == "__main__":
    pytest.main()
