from math import isnan

from config import PATH_DATA
import src.generators
import src.processing
import src.read_csv_xlsx
import src.utils
from src.widget import get_date, mask_account_card


def welcome_1() -> tuple:
    """Функция выводит приветствие и запрашивает формат файла данных"""
    transaction_data = []
    user_file_choice = 1
    print("""Привет! Добро пожаловать в программу работы
с банковскими транзакциями.""")
    norm_user_choice_file = False
    while not norm_user_choice_file:
        user_file_choice = int(input("""Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
"""))
        if user_file_choice == 1:
            norm_user_choice_file = True
            print("Для обработки выбран JSON-файл")
            transaction_data = src.utils.read_json_file(PATH_DATA / "operations.json")
        elif user_file_choice == 2:
            norm_user_choice_file = True
            print("Для обработки выбран CSV-файл")
            transaction_data = src.read_csv_xlsx.read_transactions_csv(PATH_DATA / "transactions.csv")
        elif user_file_choice == 3:
            norm_user_choice_file = True
            print("Для обработки выбран XLSX-файл")
            transaction_data = src.read_csv_xlsx.read_transactions_xlsx(PATH_DATA / "transactions_excel.xlsx")
        else:
            print("Такого варианта нет. Попробуйте ещё раз. Введите 1, 2 или 3.")
        return transaction_data, user_file_choice


def welcome_2(transaction_data: list[dict]) -> list[dict]:
    """Функция предлагает выбрать статус банковской операции и фильтрует по нему данные"""
    filtered_data_by_state = []
    norm_user_choice_status = False
    while not norm_user_choice_status:
        user_status_choice = input("""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
""")
        if user_status_choice.upper() == "EXECUTED":
            norm_user_choice_status = True
            print("Операции отфильтрованы по статусу 'EXECUTED'")
            filtered_data_by_state = src.processing.filter_by_state(transaction_data, "EXECUTED")
        elif user_status_choice.upper() == "CANCELED":
            norm_user_choice_status = True
            print("Операции отфильтрованы по статусу 'CANCELED'")
            filtered_data_by_state = src.processing.filter_by_state(transaction_data, "CANCELED")
        elif user_status_choice.upper() == "PENDING":
            norm_user_choice_status = True
            print("Операции отфильтрованы по статусу 'PENDING'")
            filtered_data_by_state = src.processing.filter_by_state(transaction_data, "PENDING")
        else:
            print(f'Статус операции "{user_status_choice}" недоступен.')
    return filtered_data_by_state


def sort_data(filtered_data: list[dict]) -> list[dict]:
    """Функция запрашивает у пользователя необходимость в сортировке данных по времени.
    Если необходимость есть, то функция уточняет у пользователя - сортировать по убыванию или по возрастанию,
    и затем сортирует данные"""
    selection = []
    norm_user_choice = False
    while not norm_user_choice:
        date_sort_flag = input("Отсортировать операции по дате? Да/Нет\n").lower()
        if date_sort_flag == "да":
            norm_user_choice = True
            norm_user_choice_order = False
            while not norm_user_choice_order:
                date_sort_order = input("Отсортировать по возрастанию или по убыванию?\n").lower()
                if date_sort_order == "по возрастанию":
                    norm_user_choice_order = True
                    selection = src.processing.sort_by_date(filtered_data, False)
                elif date_sort_order == "по убыванию":
                    norm_user_choice_order = True
                    selection = src.processing.sort_by_date(filtered_data, True)
                else:
                    print("Такого варианта нет. Введите: 'по возрастанию' или 'по убыванию'\n")
        elif date_sort_flag == "нет":
            selection = filtered_data
            norm_user_choice = True
        else:
            print("Такого варианта нет. Введите 'Да' или 'Нет'.")
    return selection


def rubble_transactions(selection: list[dict]) -> list[dict]:
    """Функция запрашивает у пользователя необходимость выводить только рублёвые транзакции.
    Если пользователь отвечает 'да', то функция фильтрует транзакции и оставляет только рублевые операции"""
    norm_user_choice = False
    while not norm_user_choice:
        rub_transactions = input("Выводить только рублевые транзакции? Да/Нет\n").lower()
        if rub_transactions == "да":
            norm_user_choice = True
            selection = list(src.generators.filter_by_currency(selection, "RUB"))
        elif rub_transactions == "нет":
            norm_user_choice = True
        else:
            print("Такого варианта нет. Введите 'Да' или 'Нет'.")
    return selection


def filter_word(selection: list[dict]) -> list[dict]:
    """Функция предлагает отфильтровать список транзакций по определённому слову в описании.
    Если пользователь соглашается и вводит слово для поиска, то функция фильтрует транзакции,
    у которых в описании есть указанное слово"""
    norm_user_choice = False
    while not norm_user_choice:
        filter_by_word = input("Отфильтровать список транзакций по определённому слову в описании? Да/Нет\n").lower()
        if filter_by_word == "да":
            norm_user_choice = True
            word = input("Введите слово для поиска\n")
            selection = src.processing.process_bank_search(selection, word)
        elif filter_by_word == "нет":
            norm_user_choice = True
        else:
            print("Такого варианта нет. Введите 'Да' или 'Нет'.")
    return selection


def display_result(selection: list[dict], num_of_file: int) -> None:
    """Функция выводит на экран список транзакций в удобном для чтения виде"""
    print("Распечатываю итоговый список транзакций...")
    len_selection = len(selection)
    print(f"Всего банковских операций в выборке: {len_selection}\n")
    if len_selection > 0:
        for transaction in selection:
            if num_of_file == 1:
                operation_date = get_date(transaction["date"])
                print(operation_date, transaction["description"])
                if "from" in transaction.keys():
                    print(f'{mask_account_card(transaction["from"])} -> {mask_account_card(transaction["to"])}')
                else:
                    print(f'{mask_account_card(transaction["to"])}')
                print(f'Сумма: {transaction["operationAmount"]["amount"]}', end='')
                print(f' {transaction["operationAmount"]["currency"]["name"]}\n')
            else:
                operation_date = get_date(transaction["date"])
                print(operation_date, transaction["description"])
                if isinstance(transaction["from"], float) and isnan(transaction["from"]):
                    print(f'{mask_account_card(transaction["to"])}')
                else:
                    print(f'{mask_account_card(transaction["from"])} -> {mask_account_card(transaction["to"])}')
                print(f'Сумма: {transaction["amount"]} {transaction["currency_name"]}\n')
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    transactions_data, file_number = welcome_1()
    filtered_transactions_data = welcome_2(transactions_data)
    sorted_data = sort_data(filtered_transactions_data)
    currency_filter = rubble_transactions(sorted_data)
    word_filter = filter_word(currency_filter)
    display_result(word_filter, file_number)
