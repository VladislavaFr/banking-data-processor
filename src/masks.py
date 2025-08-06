from logger_masks import logger

def get_mask_card_number(card_number: str) -> str | None:
    """Маскирует номер банковской карты. Формат: ХХХХ ХХ** **** ХХХХ"""
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен быть строкой из 16 цифр")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета. Формат: **ХХХХ"""
    if len(account_number) != 20 or not account_number.isdigit():
        raise ValueError("Номер счета должен быть строкой из 20 цифр")
    return f"**{account_number[-4:]}"


def test_masks_log():
    logger.debug("Функция из masks запущена")
    try:
        # логика
        logger.debug("Функция успешно выполнена")
    except Exception as e:
        logger.error(f"Ошибка: {e}")

if __name__ == "__main__":
    test_masks_log()