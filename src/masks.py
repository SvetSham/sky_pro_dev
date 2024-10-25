def get_mask_card_number(card_number: int = -1) -> str:
    """Функция маскировки номера банковской карты"""
    if card_number == -1:
        raise ValueError("Вы не ввели номер карты.")
    if not isinstance(card_number, int):
        raise ValueError("Номер карты должен содержать только цифры.")
    if len(str(card_number)) < 16:
        raise ValueError("Номер карты слишком короткий. Должно быть 16 цифр.")
    elif len(str(card_number)) > 16:
        raise ValueError("Номер карты слишком длинный. Должно быть 16 цифр.")
    mask_card_number = ""
    count = 0
    for digit in str(card_number):
        if count > 0 and count % 4 == 0:
            mask_card_number += " "
        if 0 <= count < 6 or 11 < count < 16:
            mask_card_number += str(digit)
        else:
            mask_card_number += "*"
        count += 1
    return mask_card_number


def get_mask_account(account_number: int = -1) -> str:
    """Функция маскировки номера банковского счета"""
    if account_number == -1:
        raise ValueError("Вы не ввели номер счёта.")
    if not isinstance(account_number, int):
        raise ValueError("Номер счёта должен содержать только цифры.")
    if len(str(account_number)) < 20:
        raise ValueError("Номер счёта слишком короткий. Должно быть 20 цифр.")
    elif len(str(account_number)) > 20:
        raise ValueError("Номер счёта слишком длинный. Должно быть 20 цифр.")
    mask_account = "**" + str(account_number)[-4:]
    return mask_account
