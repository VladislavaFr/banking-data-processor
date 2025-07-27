import os
import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rubles(transaction: dict) -> float:
    """
    Конвертирует сумму транзакции в рубли (RUB).

    :param transaction: Словарь с транзакцией.
    :return: Сумма в рублях (float).
    """
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")
    amount = float(transaction.get("operationAmount", {}).get("amount", 0))

    if currency == "RUB":
        return amount

    api_key = os.getenv("CURRENCY_API_KEY")
    if not api_key:
        raise ValueError("API key не найден")

    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"
    headers = {"apikey": api_key}

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()
    rate = data["rates"]["RUB"]

    return round(amount * rate, 2)
