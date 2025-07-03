from unittest.mock import call, patch

import pytest

from main import filter_word, rubble_transactions, sort_data, welcome_1, welcome_2


@pytest.fixture
def data_json() -> list[dict]:
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def transactions_list() -> list[dict]:
    transactions = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 593027.0,
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "amount": 30368.0,
            "currency_name": "Shilling",
            "currency_code": "TZS",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 5368178.0,
            "state": "PENDING",
            "date": "2020-07-07T13:57:01Z",
            "amount": 22557.0,
            "currency_name": "Yuan Renminbi",
            "currency_code": "CNY",
            "from": "Mastercard 4225154400758745",
            "to": "Mastercard 0556460753444710",
            "description": "Перевод с карты на карту",
        },
    ]
    return transactions


@pytest.fixture
def transactions_executed_only() -> list[dict]:
    transactions = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }]
    return transactions


@pytest.fixture
def transactions_canceled_only() -> list[dict]:
    transactions = [{
        "id": 593027.0,
        "state": "CANCELED",
        "date": "2023-07-22T05:02:01Z",
        "amount": 30368.0,
        "currency_name": "Shilling",
        "currency_code": "TZS",
        "from": "Visa 1959232722494097",
        "to": "Visa 6804119550473710",
        "description": "Перевод с карты на карту",
    }]
    return transactions


@pytest.fixture
def transactions_pending_only() -> list[dict]:
    transactions = [{
        "id": 5368178.0,
        "state": "PENDING",
        "date": "2020-07-07T13:57:01Z",
        "amount": 22557.0,
        "currency_name": "Yuan Renminbi",
        "currency_code": "CNY",
        "from": "Mastercard 4225154400758745",
        "to": "Mastercard 0556460753444710",
        "description": "Перевод с карты на карту",
    }]
    return transactions


@pytest.fixture
def transactions_ascending() -> list[dict]:
    transactions = [
        {
            "id": 5368178.0,
            "state": "PENDING",
            "date": "2020-07-07T13:57:01Z",
            "amount": 22557.0,
            "currency_name": "Yuan Renminbi",
            "currency_code": "CNY",
            "from": "Mastercard 4225154400758745",
            "to": "Mastercard 0556460753444710",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 593027.0,
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "amount": 30368.0,
            "currency_name": "Shilling",
            "currency_code": "TZS",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    return transactions


@pytest.fixture
def transactions_descending() -> list[dict]:
    transactions = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 593027.0,
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "amount": 30368.0,
            "currency_name": "Shilling",
            "currency_code": "TZS",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 5368178.0,
            "state": "PENDING",
            "date": "2020-07-07T13:57:01Z",
            "amount": 22557.0,
            "currency_name": "Yuan Renminbi",
            "currency_code": "CNY",
            "from": "Mastercard 4225154400758745",
            "to": "Mastercard 0556460753444710",
            "description": "Перевод с карты на карту",
        }
    ]
    return transactions


@pytest.fixture
def transaction_rubble() -> list[dict]:
    return [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }]


@pytest.fixture
def transactions_filtered_word() -> list[dict]:
    transactions = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }]
    return transactions


def test_welcome_1_json(data_json: list[dict]) -> None:
    with patch("builtins.input", return_value="1") as mock_input:
        with patch("src.utils.read_json_file", return_value=data_json) as mock_file:
            assert welcome_1() == (data_json, 1)
            mock_input.assert_called_once()
            mock_file.assert_called_once()


def test_welcome_1_csv(transactions_list: list[dict]) -> None:
    with patch("builtins.input", return_value="2") as mock_input:
        with patch("src.read_csv_xlsx.read_transactions_csv", return_value=transactions_list) as mock_file:
            assert welcome_1() == (transactions_list, 2)
            mock_input.assert_called_once()
            mock_file.assert_called_once()


def test_welcome_1_xlsx(transactions_list: list[dict]) -> None:
    with patch("builtins.input", return_value="3") as mock_input:
        with patch("src.read_csv_xlsx.read_transactions_xlsx", return_value=transactions_list) as mock_file:
            assert welcome_1() == (transactions_list, 3)
            mock_input.assert_called_once()
            mock_file.assert_called_once()


def test_welcome_2_executed(transactions_list: list[dict], transactions_executed_only: list[dict]) -> None:
    with patch("builtins.input", return_value="EXECUTED") as mock_input:
        with patch("src.processing.filter_by_state", return_value=transactions_executed_only) as mock_executed:
            assert welcome_2(transactions_list) == transactions_executed_only
            mock_input.assert_called_once()
            mock_executed.assert_called_once()


def test_welcome_2_canceled(transactions_list: list[dict], transactions_canceled_only: list[dict]) -> None:
    with patch("builtins.input", return_value="CANCELED") as mock_input:
        with patch("src.processing.filter_by_state", return_value=transactions_canceled_only) as mock_canceled:
            assert welcome_2(transactions_list) == transactions_canceled_only
            mock_input.assert_called_once()
            mock_canceled.assert_called_once()


def test_welcome_2_pending(transactions_list: list[dict], transactions_pending_only: list[dict]) -> None:
    with patch("builtins.input", return_value="PENDING") as mock_input:
        with patch("src.processing.filter_by_state", return_value=transactions_pending_only) as mock_pending:
            assert welcome_2(transactions_list) == transactions_pending_only
            mock_input.assert_called_once()
            mock_pending.assert_called_once()


def test_sort_data_no(transactions_list: list[dict]) -> None:
    with patch("builtins.input", return_value="Нет") as mock_input:
        assert sort_data(transactions_list) == transactions_list
        mock_input.assert_called_once()


def test_sort_data_yes_ascending(transactions_list: list[dict], transactions_ascending: list[dict]) -> None:
    with patch("builtins.input", side_effect=["Да", "по возрастанию"]) as mock_input:
        with patch("src.processing.sort_by_date", return_value=transactions_ascending) as mock_ascending:
            assert sort_data(transactions_list) == transactions_ascending
            mock_input.assert_has_calls([call('Отсортировать операции по дате? Да/Нет\n'),
                                         call('Отсортировать по возрастанию или по убыванию?\n')])
            mock_ascending.assert_called_once()


def test_sort_data_yes_descending(transactions_list: list[dict], transactions_descending: list[dict]) -> None:
    with patch("builtins.input", side_effect=["Да", "по убыванию"]) as mock_input:
        with patch("src.processing.sort_by_date", return_value=transactions_descending) as mock_descending:
            assert sort_data(transactions_list) == transactions_descending
            mock_input.assert_has_calls([call('Отсортировать операции по дате? Да/Нет\n'),
                                         call('Отсортировать по возрастанию или по убыванию?\n')])
            mock_descending.assert_called_once()


def test_rubble_transactions_no(transactions_list: list[dict], transaction_rubble: list[dict]) -> None:
    with patch("builtins.input", return_value="Нет") as mock_input:
        assert rubble_transactions(transactions_list) == transactions_list
        mock_input.assert_called_once()


def test_rubble_transactions_yes(transactions_list: list[dict], transaction_rubble: list[dict]) -> None:
    with patch("builtins.input", return_value="Да") as mock_input:
        assert rubble_transactions(transactions_list) == transaction_rubble
        mock_input.assert_called_once()


def test_filter_word_no(transactions_list: list[dict]) -> None:
    with patch("builtins.input", return_value="Нет") as mock_input:
        assert filter_word(transactions_list) == transactions_list
        mock_input.assert_called_once()


def test_filter_word_yes(transactions_list: list[dict], transactions_filtered_word: list[dict]) -> None:
    with patch("builtins.input", side_effect=["Да", "организации"]) as mock_input:
        assert filter_word(transactions_list) == transactions_filtered_word
        mock_input.assert_has_calls(
            [call('Отфильтровать список транзакций по определённому слову в описании? Да/Нет\n'),
             call('Введите слово для поиска\n')])
