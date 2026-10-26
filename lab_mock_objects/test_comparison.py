from unittest.mock import Mock

def fetch(value):
    return value.upper()

def test_comparison():
    mock = Mock()
    mock.fetch.side_effect = fetch

    assert mock.fetch("hello") == "HELLO"



