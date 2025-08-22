import pytest
from src.bank_project.bank_utils import process_bank_search, process_bank_operations

data = [
    {"description": "Перевод на карту", "amount": 100},
    {"description": "Оплата услуг", "amount": 200},
    {"description": "Перевод организации", "amount": 300},
]

def test_process_bank_search():
    result = process_bank_search(data, "перевод")
    assert len(result) == 2

def test_process_bank_operations():
    categories = ["Перевод", "Оплата"]
    result = process_bank_operations(data, categories)
    assert result["Перевод"] == 2
    assert result["Оплата"] == 1
