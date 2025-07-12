from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_card: str) -> str:
    """Функция обрабатывает информацию о картах и счетах, возвращает тип карта или счет и замаскированный номер"""
    info_card_split = info_card.split()
    number_card = info_card_split[-1]
    if info_card_split[0] == "Счет":
        result = f"{info_card_split[0]} {get_mask_account(int(number_card))}"
    else:
        result = f"{info_card_split[0]+" "+info_card_split[1]} {get_mask_card_number(int(number_card))}"
    return result


print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("Visa Platinum 7000792289606361"))


def get_date(date_str: str) -> str:
    """Функция возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""
    new_date_str = f"{date_str[8:10]}.{date_str[5:7]}.{date_str[:4]}"
    return new_date_str


print(get_date("2024-03-11T02:26:18.671407"))
