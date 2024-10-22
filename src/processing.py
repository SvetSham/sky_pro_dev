def filter_by_state(transaction: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция сортирует транзакции по состоянию"""
    filtered_by_state = []
    for transact in transaction:
        if state in transact.values():
            filtered_by_state.append(transact)
    return filtered_by_state
