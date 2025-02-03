import json


def read_json_file(path_to_file: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список."""
    try:
        with open(path_to_file, "rt", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        return []
    else:
        if content:
            try:
                transactions = json.loads(content)
            except json.decoder.JSONDecodeError:
                return []
        else:
            return []
        if isinstance(transactions, list):
            return transactions
        else:
            return []
