from functools import wraps
from datetime import datetime
from typing import Any, Callable, Optional
import sys
import traceback


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор автоматически логирует начало и конец выполнения функции,
    также логирует ее результаты и возникшие ошибки.
    В 'filename' - записываются логи
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            log_message = ""
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                return result
            except Exception as e:
                log_message = (
                    f"{func.__name__} error: {e.__class__.__name__}. "
                    f"Inputs: {args}, {kwargs}"
                )
                raise
            finally:
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)

        return wrapper

    return decorator


from src.decorators.log import log


@log()
def test_func(x, y):
    return x + y


test_func(2, 3)
