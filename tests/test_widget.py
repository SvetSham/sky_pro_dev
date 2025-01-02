import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_or_account, mask_card_or_account",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card_normal(card_or_account: str, mask_card_or_account: str) -> None:
    assert mask_account_card(card_or_account) == mask_card_or_account


def test_mask_account_card_short() -> None:
    with pytest.raises(ValueError):
        mask_account_card("Maestro 0")
    with pytest.raises(ValueError):
        mask_account_card("Счет 0")


def test_mask_account_card_long() -> None:
    with pytest.raises(ValueError):
        mask_account_card("Maestro 12345678910121417")
    with pytest.raises(ValueError):
        mask_account_card("Счет 123456789101214171921")


def test_mask_account_card_alpha() -> None:
    with pytest.raises(ValueError):
        mask_account_card("Maestro 1a2345678910121417")
    with pytest.raises(ValueError):
        mask_account_card("Счет 1a3456789101214171921")


def test_mask_account_card_default() -> None:
    with pytest.raises(ValueError):
        mask_account_card("Maestro ")
    with pytest.raises(ValueError):
        mask_account_card("Visa Classic ")
    with pytest.raises(ValueError):
        mask_account_card("Счет ")
    with pytest.raises(ValueError):
        mask_account_card("")


def test_get_date_normal() -> None:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_get_date_without_t() -> None:
    with pytest.raises(ValueError):
        get_date("2024-03-1102:26:18.671407")


def test_get_date_wrong_date() -> None:
    with pytest.raises(ValueError):
        get_date("2024-13-1102:26:18.671407")
    with pytest.raises(ValueError):
        get_date("2024-03-4102:26:18.671407")


def test_get_date_null() -> None:
    with pytest.raises(ValueError):
        get_date("")
