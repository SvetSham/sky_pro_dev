import pandas as pd


def read_transactions_csv(path_to_csv_file: str) -> list[dict]:
    transactions = pd.read_csv(path_to_csv_file, delimiter=";")
    return transactions.to_dict(orient="records")


def read_transactions_xlsx(path_to_xlsx_file: str) -> list[dict]:
    transactions = pd.read_excel(path_to_xlsx_file)
    return transactions.to_dict(orient="records")
