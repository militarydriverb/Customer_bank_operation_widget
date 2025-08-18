import json


def dic_list(path: str) -> list[dict]:
    """Функция принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            try:
                transactions = json.load(f)
                if isinstance(transactions, list):
                    return transactions
                else:
                    return []
            except json.JSONDecodeError:
                return []
    except FileExistsError:
        return []
    except Exception:
        return []


if __name__ == '__main__':
    path = 'data/operations.json'
    print(dic_list(path))
