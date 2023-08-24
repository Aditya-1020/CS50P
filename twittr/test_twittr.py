from twttr import shorten

def main():
    test_shorten()
    test_numbers()
    test_punctuation()

def test_shorten():
    assert shorten("Hello") == "Hll"
    assert shorten("world") == "wrld"
    assert shorten("Emojize") == "Emjz"
    assert shorten("ZEROOO") == "Zr"
    assert shorten("") == ""
    assert shorten("12345") == "12345"
    assert shorten("aeiouAEIOU") == ""
    assert shorten("This is not test") == "Ths s nt tst"

def test_numbers():
    assert shorten("1234") == "1234"


def test_punctuation():
    assert shorten("!?.,") == "!?.,"

if __name__ == "__main__":
    main()