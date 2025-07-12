def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты в виде
    числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX."""
    card_number_str = str(card_number)
    if len(card_number_str) == 16:
        mask_number = f"{card_number_str[:4]} {card_number_str[4:6]} ** **** {card_number_str[12:]}"
        return mask_number
    return "Некорректный ввод"


if __name__ == "__main__":
    print(get_mask_card_number(1234567890123456))


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета в виде числа и
    возвращает маску номера по правилу **XXXX."""
    account_number_str = str(account_number)
    if len(account_number_str) >= 4:
        mask_account = f"**{account_number_str[-4:]}"
        return mask_account
    return "Некорректный ввод"


if __name__ == "__main__":
    print(get_mask_account(1234567890123456))
