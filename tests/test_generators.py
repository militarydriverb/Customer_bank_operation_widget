import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(transactions, input_by_currency):
    currency, expected = input_by_currency
    assert list(filter_by_currency(transactions, currency)) == expected
    # for _ in range(2):
    #     assert next(filter_by_currency(transactions, "USD")) == transactions


def test_filter_by_currency_no_currency(transactions):
    assert list(filter_by_currency(transactions, "EUR")) == []


def test_transaction_descriptions(transactions):
    result = list(transaction_descriptions(transactions))
    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        'Перевод со счета на счет',
        'Перевод с карты на карту',
        'Перевод организации'
    ]


def test_transaction_description_no_transactions():
    result = list(transaction_descriptions([]))
    assert result == []


@pytest.mark.parametrize(
    'start, stop, expected',
    [
        (1, 3, ['0000 0000 0000 0001', '0000 0000 0000 0002', '0000 0000 0000 0003']),
        (10001, 10003, ['0000 0000 0001 0001', '0000 0000 0001 0002', '0000 0000 0001 0003']),
        (9999999999999998, 9999999999999999, ['9999 9999 9999 9998', '9999 9999 9999 9999']),
    ],
)
def test_card_number_generator(start, stop, expected):
    assert list(card_number_generator(start, stop)) == expected
    # generated_cards = list(card_number_generator(start, stop))
    #
    # # Проверяем, что первый и последний номера равны start и stop
    # first_card = int(generated_cards[0].replace(' ', ''))
    # last_card = int(generated_cards[-1].replace(' ', ''))
    #
    # assert first_card == start, f"Первый номер не равен start: {generated_cards[0]}"
    # assert last_card == stop, f"Последний номер не равен stop: {generated_cards[-1]}"

def test_card_number_generator_digits_number():
    with pytest.raises(ValueError) as ex_info:
        list(card_number_generator(0, 5))
    assert str(ex_info.value) == 'Число не может быть меньше 1 и больше 9999999999999999'

