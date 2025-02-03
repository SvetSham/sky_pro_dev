import os

import requests
from dotenv import load_dotenv


def get_transaction_amount(transaction: dict) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    Если транзакция была не в рублях, то сумма конвертируется в рубли."""
    source_amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        amount = source_amount
    else:
        load_dotenv()
        API_KEY = os.getenv("API_KEY")
        url = "https://api.apilayer.com/exchangerates_data/convert"
        payload = {"to": "RUB", "from": currency, "amount": source_amount}
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers, params=payload)
        amount = response.json()["result"]

    return amount
