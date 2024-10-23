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
