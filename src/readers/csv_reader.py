import pandas as pd
from typing import List, Dict

def read_transactions_csv(file_path: str) -> List[Dict]:
    """
    Считывает финансовые транзакции из CSV-файла.

    :param file_path: Путь к CSV-файлу.
    :return: Список словарей с транзакциями.
    """
    df = pd.read_csv(file_path)
    return df.to_dict(orient="records")
