def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""
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


def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера банковского счета"""
    mask_account = "**" + str(account_number)[-4:]
    return mask_account
