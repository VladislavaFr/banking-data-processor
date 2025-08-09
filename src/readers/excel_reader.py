import pandas as pd
from typing import List, Dict

def read_transactions_excel(file_path: str) -> List[Dict]:
    """
    Считывает финансовые транзакции из Excel-файла (.xlsx).

    :param file_path: Путь к Excel-файлу.
    :return: Список словарей с транзакциями.
    """
    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")
