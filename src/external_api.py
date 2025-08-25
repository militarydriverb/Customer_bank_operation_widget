import os
from typing import Optional

import requests
from dotenv import load_dotenv

from src.utils import dic_list

load_dotenv()

API_KEY = os.getenv('APILAYER_API_KEY')


def currency_rates(code_to: str, code_from: str, amount: str) -> float:
    url = f'https://api.apilayer.com/exchangerates_data/convert?to={code_to}&from={code_from}&amount={amount}'

    payload: dict = {}
    headers = {"apikey": f"{API_KEY}"}
    try:
        response = requests.request("GET", url, headers=headers, params=payload)
        status_code = response.status_code
        result = response.text

        if response.status_code != 200:
            raise Exception(f'Ошибка API: {status_code}, {result}')

    except Exception as ex_info:
        raise Exception(f'Что-то пошло не так. {str(ex_info)}')
    else:
        output_data = response.json()
        return round(float(output_data.get('result', 0)), 2)


def transactions_by_currency(operation: Optional[dict]) -> None | int | float:
    """ Функция конвертация транзакции в рубли по актуальному курсу"""

    try:
        if not operation:
            print("Словарь пуст")
            return 0
        currency_code = operation["operationAmount"]["currency"]["code"]
        amount_value = operation["operationAmount"]["amount"]

        if currency_code == "RUB":
            result = round(float(amount_value), 2)
        else:
            result = currency_rates(code_to='RUB', code_from=currency_code, amount=amount_value)
        return result
    except Exception as e:
        print(str(e))
    return None


if __name__ == '__main__':
    data_str = dic_list('../data/operations.json')  # pragma: no cover
    print(transactions_by_currency(data_str[1]))  # pragma: no cover
