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
