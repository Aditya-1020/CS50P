import pytest
from fuel import convert, gauge

def main():
    test_convert_valid_fraction()
    test_convert_invalid_fraction()
    test_gauge()
    test_gauge_invalid()


def test_convert_valid_fraction():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("2/3") == 67

def test_convert_invalid_fraction():
    with pytest.raises(ValueError):
        convert("3/0")
    with pytest.raises(ValueError):
        convert("-2/5")
    with pytest.raises(ValueError):
        convert("4.5/7")
    with pytest.raises(ValueError):
        convert("5/4")

def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(0) == "0%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "100%"
    assert gauge(-5) == "-5%"

def test_gauge_invalid():
    assert gauge(None) == "Invalid"
    assert gauge("test") == "test"

if __name__ == "__main__":
    main()