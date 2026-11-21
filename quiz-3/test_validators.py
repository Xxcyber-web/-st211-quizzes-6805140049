import pytest
from validators import validate_email, validate_age


def test_valid_email():
    assert validate_email("student@example.com") is True


def test_invalid_email():
    with pytest.raises(ValueError):
        validate_email("invalid-email")


def test_valid_age():
    assert validate_age(25) is True


def test_invalid_age():
    with pytest.raises(ValueError):
        validate_age(-1)


def test_age_above_limit():
    with pytest.raises(ValueError):
        validate_age(151)


def test_age_wrong_type():
    with pytest.raises(TypeError):
        validate_age("twenty")