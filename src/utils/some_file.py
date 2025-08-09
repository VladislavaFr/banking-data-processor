from src.utils.logger import logger

def test_utils_log():
    logger.debug("Функция из utils запущена")
    try:
        # тут могла быть твоя логика
        logger.debug("Функция выполнена успешно")
    except Exception as e:
        logger.error(f"Ошибка: {e}")