from pathlib import Path

import pandas as pd
from config import PATH_DATA


def read_transactions_csv(path_to_csv_file: str | Path) -> list[dict]:
    """Функция принимает на вход путь к csv-файлу с финансовыми транзакциями
    и считывает его в список словарей"""
    transactions = pd.read_csv(path_to_csv_file, delimiter=";")
    print(transactions.to_dict(orient="records"))
    return transactions.to_dict(orient="records")


read_transactions_csv(PATH_DATA / "transactions.csv")


def read_transactions_xlsx(path_to_xlsx_file: str | Path) -> list[dict]:
    """Функция принимает на вход путь к xlsx-файлу с финансовыми транзакциями
    и считывает его в список словарей"""
    transactions = pd.read_excel(path_to_xlsx_file)
    return transactions.to_dict(orient="records")
