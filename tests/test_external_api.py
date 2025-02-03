import os
from unittest.mock import patch

import pytest
from dotenv import load_dotenv

from src.external_api import get_transaction_amount


@pytest.fixture
def my_API_KEY():
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    return API_KEY


@pytest.fixture
def transaction_usd():
    transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "1000.0", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    return transaction


@pytest.fixture
def transaction_rub():
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    return transaction


@patch("requests.get")
def test_get_transaction_amount_usd(mock_get, transaction_usd, my_API_KEY):
    mock_get.return_value.json.return_value = {"result": 100000.0}
    assert get_transaction_amount(transaction_usd) == 100000.0
    payload = {"to": "RUB", "from": "USD", "amount": 1000.0}
    headers = {"apikey": my_API_KEY}
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert", headers=headers, params=payload
    )


def test_get_transaction_amount_rub(transaction_rub):
    assert get_transaction_amount(transaction_rub) == 31957.58
