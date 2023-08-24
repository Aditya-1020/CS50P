import pytest
from seasons import check_date

def test_check_date():
    assert check_date("1998-07-03") == ("1998", "07", "03")
    with pytest.raises(ValueError, match="Invalid date"):
        check_date("1998-7-3")
    with pytest.raises(ValueError, match="Invalid date"):
        check_date("july 3, 1998")

if __name__ == "__main__":
    test_check_date()
