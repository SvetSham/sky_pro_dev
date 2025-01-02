import time
from collections.abc import Callable
from functools import wraps
from typing import Any


def log(filename: str="") -> Callable:
    """Декоратор регистрирует время вызова и останова функции, имя функции, передаваемые аргументы,
    результат выполнения и информацию об ошибках"""

    def my_log(function: Callable) -> Callable:
        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> None:
            message = " ok\n"
            result = None
            start = "start: " + str(time.time()) + "\n"
            try:
                result = function(*args, **kwargs)
            except Exception as e:
                message = f" error: {e}. Inputs: {tuple(args)}, {dict(kwargs)}\n"
            stop = "stop: " + str(time.time()) + "\n"
            res = "result = " + str(result) + "\n"
            if filename == "":
                print(start, wrapper.__name__ + message, stop, res)  # печать в консоль
            else:
                with open(filename, "a", encoding="utf-8") as log_file:
                    log_file.write(start + wrapper.__name__ + message + stop + res)  # запись лога в файл

        return wrapper

    return my_log
