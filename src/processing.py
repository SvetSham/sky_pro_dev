import re
from collections import Counter

def filter_by_state(transaction: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция фильтрует транзакции по состоянию"""
    filtered_by_state = []
    for transact in transaction:
        if state in transact.values():
            filtered_by_state.append(transact)
    return filtered_by_state


def sort_by_date(transaction: list[dict], in_descending_order: bool = True) -> list[dict]:
    """Функция сортирует транзакции по дате по убыванию или по возрастанию"""
    sorted_transaction = sorted(transaction, key=lambda x: x["date"], reverse=in_descending_order)
    return sorted_transaction


def process_bank_search(data: list[dict], str_for_search: str) -> list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    и возвращает список словарей, у которых в описании есть данная строка."""
    found_data = []
    for transaction in data:
        if re.search(str_for_search, transaction["description"], flags=re.IGNORECASE):
            found_data.append(transaction)
    return found_data


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    и возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    operations_in_categories = []
    for transaction in data:
        operations_in_categories.append(transaction["description"])
    num_operations_in_categories = Counter(operations_in_categories)
    return dict(num_operations_in_categories)
