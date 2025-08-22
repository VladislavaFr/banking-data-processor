from typing import Any, List, Dict
import re
from collections import Counter


def process_bank_search(data: List[Dict[str, Any]], search: str) -> List[Dict[str, Any]]:
    """
    Фильтрует список банковских операций по заданной строке в поле description.

    Args:
        data: Список словарей с операциями.
        search: Строка для поиска в описании.

    Returns:
        Список словарей, где description содержит search.
    """
    search_lower = search.lower()
    filtered = [
        item for item in data
        if search_lower in str(item.get('description', '')).lower()
    ]
    return filtered


def process_bank_operations(data: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по каждой категории.

    Args:
        data: Список словарей с операциями.
        categories: Список категорий для подсчета (по description).

    Returns:
        Словарь: {категория: количество операций}.
    """
    counts: Dict[str, int] = {}
    for category in categories:
        cnt = sum(
            1 for item in data
            if category.lower() in str(item.get('description', '')).lower()
        )
        counts[category] = cnt
    return counts
