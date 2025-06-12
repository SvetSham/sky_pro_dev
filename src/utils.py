import json
import logging
import os


if os.path.basename(os.getcwd()) == "HomeWork_9.1":
    filename = "logs/utils.log"
else:
    filename = "../logs/utils.log"

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(filename, encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_json_file(path_to_file: str) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список."""
    try:
        with open(path_to_file, "rt", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError as fnf:
        logger.error(f"Произошла ошибка: {fnf}")
        return []
    else:
        logger.info("Файл открыт успешно")
        if content:
            logger.info("Файл прочитан")
            try:
                transactions = json.loads(content)
            except json.decoder.JSONDecodeError as jse:
                logger.error(f"Произошла ошибка: {jse}")
                return []
            else:
                logger.info("Десериализация прошла успешно")
        else:
            logger.error("Файл пуст")
            return []
        if isinstance(transactions, list):
            logger.info("Получен список")
            return transactions
        else:
            logger.error("Получен не список")
            return []
