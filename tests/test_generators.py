import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def operation() -> list[dict]:
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
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
    return transactions


@pytest.fixture
def operation_filtered_usd() -> list[dict]:
    transactions_usd = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]
    return transactions_usd


@pytest.fixture
def empty_list() -> list[dict]:
    empty: list[dict] = [{}]
    return empty


@pytest.fixture
def descriptions() -> list[str]:
    description = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    return description


def test_filter_by_currency_found_usd(operation: list[dict], operation_filtered_usd: list[dict]) -> None:
    result = []
    for el in filter_by_currency(operation, "USD"):
        result.append(el)
    assert result == operation_filtered_usd


def test_filter_by_currency_not_found_cny(operation: list[dict]) -> None:
    result = []
    for el in filter_by_currency(operation, "CNY"):
        result.append(el)
    assert result == []


def test_filter_by_currency_empty(empty_list: list[dict]) -> None:
    result = []
    for el in filter_by_currency(empty_list, "USD"):
        result.append(el)
    assert result == []


def test_transaction_descriptions_normal(operation: list[dict], descriptions: list[str]) -> None:
    result = []
    for el in transaction_descriptions(operation):
        result.append(el)
    assert result == descriptions


def test_transaction_descriptions_empty(empty_list: list[dict]) -> None:
    result = []
    for el in transaction_descriptions(empty_list):
        result.append(el)
    assert result == []


@pytest.mark.parametrize(
    "start, stop, expected_numbers",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (9999999999999997, 9999999999999999, ["9999 9999 9999 9997", "9999 9999 9999 9998", "9999 9999 9999 9999"]),
    ],
)
def test_card_number_generator(start: int, stop: int, expected_numbers: list) -> None:
    result = []
    for el in card_number_generator(start, stop):
        result.append(el)
    assert result == expected_numbers


def test_card_number_generator_reverse() -> None:
    with pytest.raises(ValueError):
        next(card_number_generator(5, 1))


def test_card_number_generator_max() -> None:
    with pytest.raises(ValueError):
        next(card_number_generator(9999999999999999, 10000000000000000))
