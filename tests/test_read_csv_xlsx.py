import unittest
from unittest.mock import patch

import pandas as pd
import pytest

from config import PATH_DATA
from src.read_csv_xlsx import read_transactions_csv, read_transactions_xlsx


@pytest.fixture
def transactions_df() -> pd.DataFrame:
    transactions = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]
    df = pd.DataFrame(transactions)
    return df


@pytest.fixture
def transactions_list() -> list[dict]:
    transactions = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]
    return transactions


@patch("pandas.read_csv")
def test_read_transactions_csv(
        mock_csv: unittest.mock.MagicMock,
        transactions_df: pd.DataFrame,
        transactions_list: list[dict]
) -> None:
    mock_csv.return_value = transactions_df
    path_to_csv_file = PATH_DATA / "transactions.csv"
    result = read_transactions_csv(path_to_csv_file)
    assert result == transactions_list
    mock_csv.assert_called_once_with(path_to_csv_file, delimiter=";")


@patch("pandas.read_excel")
def test_read_transactions_xlsx(
        mock_xlsx: unittest.mock.MagicMock,
        transactions_df: pd.DataFrame,
        transactions_list: list[dict]
) -> None:
    mock_xlsx.return_value = transactions_df
    path_to_xlsx_file = PATH_DATA / "transactions_excel.xlsx"
    result = read_transactions_xlsx(path_to_xlsx_file)
    assert result == transactions_list
    mock_xlsx.assert_called_once_with(path_to_xlsx_file)
