import logging
import os

if os.path.basename(os.getcwd()) == "HomeWork_9.1":
    filename = "logs/masks.log"
else:
    filename = "../logs/masks.log"

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(filename, encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str = '-1') -> str:
    """Функция маскировки номера банковской карты"""
    if card_number == '-1':
        logger.error("Номер карты не введён")
        raise ValueError("Вы не ввели номер карты.")
    if not card_number.isdigit():
        logger.error("Номер карты - не число")
        raise ValueError("Номер карты должен содержать только цифры.")
    if len(card_number) < 16:
        logger.error("Номер карты короче 16 цифр")
        raise ValueError("Номер карты слишком короткий. Должно быть 16 цифр.")
    elif len(card_number) > 16:
        logger.error("Номер карты длиннее 16 цифр")
        raise ValueError("Номер карты слишком длинный. Должно быть 16 цифр.")
    else:
        logger.info("Номер карты получен")
    mask_card_number = ""
    count = 0
    for digit in card_number:
        if count > 0 and count % 4 == 0:
            mask_card_number += " "
        if 0 <= count < 6 or 11 < count < 16:
            mask_card_number += digit
        else:
            mask_card_number += "*"
        count += 1
    logger.info("Номер карты замаскирован")
    return mask_card_number


def get_mask_account(account_number: int = -1) -> str:
    """Функция маскировки номера банковского счета"""
    if account_number == -1:
        logger.error('Номер счёта не введён')
        raise ValueError("Вы не ввели номер счёта.")
    if not isinstance(account_number, int):
        logger.error('Номер счёта - не число')
        raise ValueError("Номер счёта должен содержать только цифры.")
    if len(str(account_number)) < 20:
        logger.error('Номер счёта короче 20 цифр')
        raise ValueError("Номер счёта слишком короткий. Должно быть 20 цифр.")
    elif len(str(account_number)) > 20:
        logger.error('Номер счёта длиннее 20 цифр')
        raise ValueError("Номер счёта слишком длинный. Должно быть 20 цифр.")
    mask_account = "**" + str(account_number)[-4:]
    logger.info('Номер счёта замаскирован')
    return mask_account
