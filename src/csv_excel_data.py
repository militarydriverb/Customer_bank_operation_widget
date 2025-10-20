import json
from json import JSONDecodeError
from pprint import pprint

import pandas as pd


def get_csv_data_reading(file_path: str) -> list[dict] | None:
    """Функция считывает финансовые операции из CSV файла и выдает список словарей с транзакциями"""
    try:
        df = pd.read_csv(file_path, delimiter=";")
        return df.to_dict("records")
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    file_path = "../data/transactions.csv"  # pragma: no cover
    result = get_csv_data_reading(file_path)  # pragma: no cover
    pprint(result)  # pragma: no cover
    print("Конец CSV файла")  # pragma: no cover
    print()  # pragma: no cover


def get_excel_data_reading(file_path1: str):
    """Функция считывает финансовые операции из Excel файла и выдает список словарей с транзакциями"""
    try:
        df = pd.read_excel(file_path1)
        transaction = df.to_dict("records")
        return json.dumps(transaction, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        return ""
    except JSONDecodeError:
        return ""


if __name__ == "__main__":
    file_path1 = "../data/transactions_excel.xlsx"  # pragma: no cover
    result = get_excel_data_reading(file_path1)  # pragma: no cover
    print(result)  # pragma: no cover
    print("Конец Excel файла")  # pragma: no cover
