from unittest.mock import patch
import pytest
from project import generate_password, validate_password

def test_generate_password():
    # Mock user input for password length
    with patch("builtins.input", side_effect=["12", "y", "y", "y", "n"]):
        generated_password = generate_password()
    assert len(generated_password) >= 6

def test_validate_password_valid():
    valid_password = "StrongP@ssw0rd"
    assert validate_password(valid_password) is True

def test_validate_password_invalid_length():
    invalid_password = "WeakPass123"
    assert validate_password(invalid_password) is False

def test_validate_password_invalid_characters():
    invalid_password = "WeakPassword"
    assert validate_password(invalid_password) is False

if __name__ == "__main__":
    pytest.main()