import json
from typing import Any
from pathlib import Path


def read_json_file(path: str) -> list[dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список словарей.
    Если файл не найден, пустой или содержит не список — возвращает пустой список.
    """
    try:
        file_path = Path(path)
        if not file_path.exists():
            return []

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except Exception:
        return []
