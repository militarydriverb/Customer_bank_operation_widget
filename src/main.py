import os

from src.bank_search import process_bank_search
from src.csv_excel_data import get_csv_data_reading, get_excel_data_reading
from src.processing import filter_by_state, sort_by_date
from src.utils import dic_list

json_path = os.path.join(os.getcwd(), "..", "data", "operations.json")
csv_path = os.path.join(os.getcwd(), "..", "data", "transactions.csv")
xlsx_path = os.path.join(os.getcwd(), "..", "data", "transactions_excel.xlsx")


def main():
    print("Текущая директория:", os.getcwd())
    print("JSON-файл существует?", os.path.exists(json_path))
    print("CSV-файл существует?", os.path.exists(csv_path))
    print("XLSX-файл существует?", os.path.exists(xlsx_path))

    print(
        "Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями."
    )
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    # Выбор формата файла
    file_format = input()

    if file_format == "1":
        print("Программа: Для обработки выбран JSON-файл.")
        transactions = dic_list(json_path)
        print(transactions)
    elif file_format == "2":
        print("Программа: Для обработки выбран CSV-файл.")
        transactions = get_csv_data_reading(csv_path)
    elif file_format == "3":
        print("Программа: Для обработки выбран XLSX-файл.")
        transactions = get_excel_data_reading(xlsx_path)
    else:
        print("Программа: Неверный формат файла. Завершение работы.")
        return

    # Фильтрация по статусу
    valid_states = ["EXECUTED", "CANCELED", "PENDING"]
    state = ""
    while state not in valid_states:
        print("Программа: Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтрации статусы:", ", ".join(valid_states))
        state = input().strip().upper()

        if state not in valid_states:
            print(f"Программа: Статус операции '{state}' недоступен.")

    filtered_transactions = filter_by_state(transactions, state)
    print(filtered_transactions)
    print(f"Программа: Операции отфильтрованы по статусу '{state}'")

    # Сортировка по дате
    sort_date = (
        input("Программа: Отсортировать операции по дате? Да/Нет\n").strip().lower()
    )
    if sort_date in ["да", "yes"]:
        sort_order = (
            input("Программа: Отсортировать по возрастанию или по убыванию?\n")
            .strip()
            .lower()
        )
        filtered_transactions = sort_by_date(
            filtered_transactions,
            descending=(sort_order in ["по возрастанию", "ascending"]),
        )
    print(filtered_transactions)
    # Фильтрация по валюте
    rub_filter = (
        input("Программа: Выводить только рублевые транзакции? Да/Нет\n")
        .strip()
        .lower()
    )
    if rub_filter in ["да", "yes"]:
        filtered_transactions = [
            tx
            for tx in transactions
            if tx.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
        ]
        print(filtered_transactions)
    # Фильтрация по слову в описании
    word_filter = (
        input(
            "Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n"
        )
        .strip()
        .lower()
    )
    if word_filter in ["да", "yes"]:
        search_word = input("Программа: Введите слово для поиска:\n").strip().lower()
        filtered_transactions = process_bank_search(filtered_transactions, search_word)

    # Вывод результата

    print("Программа: Распечатываю итоговый список транзакций...")
    print(filtered_transactions)
    if not filtered_transactions:
        print(
            "Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
        )
        return

    print(
        f"Программа: Всего банковских операций в выборке: {len(filtered_transactions)}"
    )


if __name__ == "__main__":
    main()
