from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция возвращает маску для номера карты или счёта"""
    description_account_card = account_card.split()
    print(description_account_card)
    result: str
    if description_account_card[0] == "Счет":
        if len(description_account_card) < 2:
            raise ValueError("Вы не ввели номер счёта.")
        account_number: int
        try:
            account_number = int(description_account_card[1])
        except ValueError:
            raise ValueError("Номер счёта должен содержать только цифры.")
        result = description_account_card[0] + " " + get_mask_account(account_number)
    else:
        if len(description_account_card) < 2:
            raise ValueError("Вы не ввели номер карты.")
        if description_account_card[-1].isalpha():
            raise ValueError("Вы не ввели номер карты.")
        card_number: int
        try:
            card_number = int(description_account_card[-1])
        except ValueError:
            raise ValueError("Номер карты должен содержать только цифры.")
        result = get_mask_card_number(card_number)
        result = " ".join(description_account_card[:-1]) + " " + result
    return result


def get_date(date: str) -> str:
    """Функция преобразует дату из формата '2024-03-11T02:26:18.671407' в формат 'ДД.ММ.ГГГГ'"""
    if len(date) == 0:
        raise ValueError("Дата не передана.")
    if "T" in date:
        date_old = date.split("T")
    else:
        raise ValueError("Проверьте формат даты.")
    date_new = date_old[0].split("-")
    date_old.clear()
    date_old = date_new[::-1]
    if int(date_old[1]) < 1 or int(date_old[1]) > 12:
        raise ValueError("Проверьте месяц в дате.")
    if int(date_old[0]) < 1 or int(date_old[0]) > 31:
        raise ValueError("Проверьте день в дате.")
    result = ".".join(date_old)
    return result
