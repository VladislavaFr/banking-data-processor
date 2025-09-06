from typing import Any, List, Dict
from src.bank_project.bank_utils import process_bank_search, process_bank_operations


def main() -> None:
    """
    Основная функция проекта. Предоставляет пользовательский интерфейс
    для работы с банковскими транзакциями.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Выбор источника данных
    while True:
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        choice = input("Пользователь: ").strip()
        if choice in {"1", "2", "3"}:
            break
        print("Некорректный ввод. Попробуйте еще раз.")

    if choice == "1":
        print("Программа: Для обработки выбран JSON-файл.")
    elif choice == "2":
        print("Программа: Для обработки выбран CSV-файл.")
    else:
        print("Программа: Для обработки выбран XLSX-файл.")

    # Пример: заглушка для данных
    data: List[Dict[str, Any]] = [
        {"description": "EXECUTED перевод", "amount": 1000, "currency": "RUB"},
        {"description": "CANCELED снятие", "amount": 500, "currency": "RUB"},
        {"description": "EXECUTED пополнение", "amount": 1500, "currency": "USD"},
    ]

    # Фильтр по статусу
    valid_status = {"EXECUTED", "CANCELED", "PENDING"}
    while True:
        status = input("Введите статус, по которому необходимо выполнить фильтрацию: ").strip().upper()
        if status in valid_status:
            break
        print(f'Статус операции "{status}" недоступен.')

    filtered_data = process_bank_search(data, status)
    print(f'Программа: Операции отфильтрованы по статусу "{status}"')

    # Пример дополнительных вопросов
    sort_answer = input("Отсортировать операции по дате? Да/Нет ").strip().lower()
    if sort_answer == "да":
        order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        # Заглушка сортировки
        filtered_data.sort(key=lambda x: x.get("amount", 0), reverse=(order == "по убыванию"))

    rub_answer = input("Выводить только рублевые транзакции? Да/Нет ").strip().lower()
    if rub_answer == "да":
        filtered_data = [x for x in filtered_data if x.get("currency") == "RUB"]

    search_answer = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет ").strip().lower()
    if search_answer == "да":
        word = input("Введите слово для фильтрации: ").strip()
        filtered_data = process_bank_search(filtered_data, word)

    print("Программа: Распечатываю итоговый список транзакций...")

    if not filtered_data:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(filtered_data)}\n")
        for item in filtered_data:
            print(f"{item.get('description')} | Сумма: {item.get('amount')} {item.get('currency')}")
