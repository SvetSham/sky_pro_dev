import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def operations() -> list[dict]:
    transactions = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    return transactions


@pytest.fixture
def operations_same_date() -> list[dict]:
    transactions = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    return transactions


@pytest.fixture
def operations_same_date_sorted_direct() -> list[dict]:
    transactions = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    return transactions


@pytest.fixture
def operations_same_date_sorted_reverse() -> list[dict]:
    transactions = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    return transactions


@pytest.fixture
def executed_operations() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def canceled_operations() -> list[dict]:
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def sorted_operations_direct() -> list[dict]:
    sorted_direct = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    return sorted_direct


@pytest.fixture
def sorted_operations_reverse() -> list[dict]:
    sorted_reverse = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    return sorted_reverse


"""@pytest.mark.parametrize("operation, state, result", [('operations', None, 'executed_operations'),
                                                      ('operations', "EXECUTED", 'executed_operations'),
                                                      ('operations', "CANCELED", 'canceled_operations')
                                                      ])
def test_filter_by_state_normal(operation: list[dict], state: str, result: list[dict], request) -> None:
    assert filter_by_state(request.getfixturevalue(operation), state) == request.getfixturevalue(result)"""


def test_filter_by_state_normal(
    operations: list[dict], executed_operations: list[dict], canceled_operations: list[dict]
) -> None:
    assert filter_by_state(operations) == executed_operations
    assert filter_by_state(operations, "EXECUTED") == executed_operations
    assert filter_by_state(operations, "CANCELED") == canceled_operations


def test_filter_by_state_not_found(executed_operations: list[dict], canceled_operations: list[dict]) -> None:
    assert filter_by_state(executed_operations, "CANCELED") == []
    assert filter_by_state(canceled_operations, "EXECUTED") == []
    assert filter_by_state(canceled_operations) == []


def test_sort_by_date_normal(
    operations: list[dict], sorted_operations_direct: list[dict], sorted_operations_reverse: list[dict]
) -> None:
    assert sort_by_date(operations) == sorted_operations_direct
    assert sort_by_date(operations, True) == sorted_operations_direct
    assert sort_by_date(operations, False) == sorted_operations_reverse


def test_sort_by_date_same_date(
    operations_same_date: list[dict],
    operations_same_date_sorted_direct: list[dict],
    operations_same_date_sorted_reverse: list[dict],
) -> None:
    assert sort_by_date(operations_same_date) == operations_same_date_sorted_direct
    assert sort_by_date(operations_same_date, True) == operations_same_date_sorted_direct
    assert sort_by_date(operations_same_date, False) == operations_same_date_sorted_reverse
