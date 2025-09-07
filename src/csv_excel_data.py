import json
from pprint import pprint

import pandas as pd


def get_csv_data_reading(file_path: str) -> list[dict] | None:
    """Функция считывает финансовые операции из CSV файла и выдает список словарей с транзакциями"""
    try:
        df = pd.read_csv(file_path, delimiter=';')
        return df.to_dict('records')
    except FileNotFoundError:
        return []


if __name__ == '__main__':
    file_path = 'transactions.csv'
    result = get_csv_data_reading(file_path)
    pprint(result)
    print("Конец CSV файла")
    print()


def get_excel_data_reading(file_path1: str):
    """Функция считывает финансовые операции из Excel файла и выдает список словарей с транзакциями"""
    try:
        df = pd.read_excel(file_path1)
        transaction = df.to_dict('records')
        return json.dumps(transaction, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        return ''


if __name__ == '__main__':
    file_path1 = 'transactions_excel.xlsx'
    result = get_excel_data_reading(file_path1)
    print(result)
    print("Конец Excel файла")
