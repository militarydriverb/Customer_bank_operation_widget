import json

from src.csv_excel_data import get_excel_data_reading


def process_bank_operations(
    data: list[dict], categories: list[str] = None
) -> dict[str, int]:
    """
    Функция, которая принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    Категории операций хранятся в поле description.
    Args:
        data (list[dict]): Список транзакций.
        categories(list[str]): Список категорий операций

    Returns:
        dict(key: str = category, value: int = count of transactions):
    """
    if not isinstance(data, list):
        return {}

    result = {}
    categories = set(categories) if categories else None  # Для оптимизации поиска

    for transaction in data:
        if not isinstance(transaction, dict):
            continue

        description = str(transaction.get("description", "")).strip().lower()
        # Если description содержит только мусор (например, "nan", "") — присваиваем "без категории или пустая категория"
        if not description or description in ["nan", ""]:
            category = "без категории или пустая категория"
        else:
            category = description
        # Если переданы категории — учитываем только их
        if categories is not None and category not in categories:
            continue

        if category in result:
            result[category] += 1
        else:
            result[category] = 1

    return result


if __name__ == "__main__":
    file_path = "../transactions_excel.xlsx"
    data_str = get_excel_data_reading(file_path)

    try:
        data = json.loads(data_str)
    except json.JSONDecodeError:
        print("Ошибка: Полученные данные не являются корректным JSON.")
        data = []

    if isinstance(data, list):
        #  Подсчёт всех категорий
        all_categories_count = process_bank_operations(data)
        print("\nКоличество операций по категориям:")
        for category, count in all_categories_count.items():
            print(f"{category}: {count}")
