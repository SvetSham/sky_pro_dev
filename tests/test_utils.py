import os
from unittest.mock import mock_open, patch

import pytest

from src.utils import read_json_file


@pytest.fixture
def file_content():
    content = """[{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
    }]"""
    return content


@pytest.fixture
def path_to_file():
    if os.path.basename(os.getcwd()) == "HomeWork_9.1":
        filename = "data/operations.json"
    else:
        filename = "../data/operations.json"
    return filename


def test_read_json_file_with_data(file_content, path_to_file):
    with patch("builtins.open", mock_open(read_data=file_content)) as mock_file:
        result = read_json_file(path_to_file)
        assert result == [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        ]

        mock_file.assert_called_once_with(path_to_file, "rt", encoding="utf-8")


def test_read_json_file_empty(path_to_file):
    with patch("builtins.open", mock_open(read_data="")) as mock_file:
        result = read_json_file(path_to_file)
        assert result == []
        mock_file.assert_called_once_with(path_to_file, "rt", encoding="utf-8")


def test_read_json_file_not_list(path_to_file):
    with patch("builtins.open", mock_open(read_data="{}")) as mock_file:
        result = read_json_file(path_to_file)
        assert result == []
        mock_file.assert_called_once_with(path_to_file, "rt", encoding="utf-8")


def test_read_json_file_not_found():
    assert read_json_file("file_not_exists.json") == []
