def filter_by_currency(transactions: list[dict], currency: str):
    """Функция фильтрует транзакции по указанной валюте"""
    for transaction in transactions:
        if "operationAmount" in transaction.keys():
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction


def transaction_descriptions(transactions: list[dict]):
    """Функция возвращает описание транзакций"""
    for transaction in transactions:
        if "description" in transaction.keys():
            yield transaction["description"]


def card_number_generator(start: int, stop: int):
    """Функция генерирует номера карт в заданном диапазоне"""
    if start > stop:
        raise ValueError("Последовательность 'страт, стоп' должна быть возрастающей.")
    if stop > 9999999999999999:
        raise ValueError("Числа должны быть 16-ти-значными.")
    for i in range(start, stop + 1):
        result_str = str(i).rjust(16, "0")
        result = f"{result_str[:4]} {result_str[4:8]} {result_str[8:12]} {result_str[12:]}"
        yield result
