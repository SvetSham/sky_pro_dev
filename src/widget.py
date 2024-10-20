def mask_account_card(account_card: str) -> str:
    """Функция возвращает маску для номера карты или счёта"""
    import masks

    description_account_card = account_card.split()
    result = ""
    if description_account_card[0] == "Счет":
        result = description_account_card[0] + " " + masks.get_mask_account(int(description_account_card[1]))
    else:
        result = masks.get_mask_card_number(int(description_account_card[-1]))
        result = " ".join(description_account_card[:-1]) + " " + result

    return result


def get_date(date: str) -> str:
    """Функция преобразует дату из формата '2024-03-11T02:26:18.671407' в формат 'ДД.ММ.ГГГГ'"""
    date_old = date.split("T")
    date_new = date_old[0].split("-")
    date_old.clear()
    date_old = date_new[::-1]
    result = ".".join(date_old)
    return result
