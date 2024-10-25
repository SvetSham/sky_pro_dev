import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("input_int, output_str", [(1596837868705199, "1596 83** **** 5199")])
def test_get_mask_card_number_normal(input_int: int, output_str: str) -> None:
    assert get_mask_card_number(input_int) == output_str


def test_get_mask_card_number_short() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(0)


def test_get_mask_card_number_long() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(12345678910121417)


def test_get_mask_card_number_alpha() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("1a")


def test_get_mask_card_number_default() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number()


def test_get_mask_account_normal() -> None:
    assert get_mask_account(64686473678894779589) == "**9589"


def test_get_mask_account_short() -> None:
    with pytest.raises(ValueError):
        get_mask_account(0)


def test_get_mask_account_long() -> None:
    with pytest.raises(ValueError):
        get_mask_account(123456789101214171921)


def test_get_mask_account_alpha() -> None:
    with pytest.raises(ValueError):
        get_mask_account("1a")


def test_get_mask_account_default() -> None:
    with pytest.raises(ValueError):
        get_mask_account()
