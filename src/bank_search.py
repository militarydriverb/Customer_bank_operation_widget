import json
import re

from src.csv_excel_data import get_excel_data_reading


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Функция, которая принимает список словарей с данными о банковских операциях и строку поиска,
     а возвращать список словарей, у которых в описании есть данная строка (поиск нечувствителен к регистру).
      Args:
        data (list[dict]): Список транзакций.
        search (str): Подстрока для поиска в описании.

    Returns:
        list[dict]: Отфильтрованный список транзакций
    """
    if not isinstance(search, str) or not search.strip():
        return []

    search_pattern = re.compile(re.escape(search), flags=re.IGNORECASE)
    result = []

    for transaction in data:
        if not isinstance(transaction, dict):
            continue  # Пропускаем, если элемент не является словарём

        description = transaction.get("description")
        if not isinstance(description, (str, float)):
            continue  # Пропускаем, если описание не строка и не число

        if search_pattern.search(str(description)):
            result.append(transaction)

    return result


if __name__ == "__main__":
    file_path = "../data/transactions_excel.xlsx"
    data_str = get_excel_data_reading(file_path)  # <-- Это JSON-строка

    try:
        data = json.loads(data_str)  # <-- Преобразуем строку в список словарей
    except json.JSONDecodeError:
        print("Ошибка: Полученные данные не являются корректным JSON.")
        data = []

    if isinstance(data, list):
        filtered_data = process_bank_search(data, "Перевод с карты на карту")
        print(f"Найдено {len(filtered_data)} транзакций:")
        for tx in filtered_data:
            print(tx)
    else:
        print("Ошибка: данные не являются списком транзакций.")
        print("Полученные данные:", data)
