from math import isnan

from config import PATH_DATA
from src.generators import filter_by_currency
from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.read_csv_xlsx import read_transactions_csv, read_transactions_xlsx
from src.utils import read_json_file
from src.widget import get_date, mask_account_card

transaction_data = []
filtered_data_by_state = []
selection = []
user_file_choice = 1

print("""Привет! Добро пожаловать в программу работы
с банковскими транзакциями.""")
norm_user_choice = False
while not norm_user_choice:
    user_file_choice = int(
        input(
            ("""Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
""")))
    if user_file_choice == 1:
        norm_user_choice = True
        print("Для обработки выбран JSON-файл")
        transaction_data = read_json_file(PATH_DATA / "operations.json")
    elif user_file_choice == 2:
        norm_user_choice = True
        print("Для обработки выбран CSV-файл")
        transaction_data = read_transactions_csv(PATH_DATA / "transactions.csv")
    elif user_file_choice == 3:
        norm_user_choice = True
        print("Для обработки выбран XLSX-файл")
        transaction_data = read_transactions_xlsx(PATH_DATA / "transactions_excel.xlsx")
    else:
        print("Такого варианта нет. Попробуйте ещё раз.")

norm_user_choice = False
while not norm_user_choice:
    user_status_choice = input("""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
""")
    if user_status_choice.upper() == "EXECUTED":
        norm_user_choice = True
        print("Операции отфильтрованы по статусу 'EXECUTED'")
        filtered_data_by_state = filter_by_state(transaction_data, "EXECUTED")
    elif user_status_choice.upper() == "CANCELED":
        norm_user_choice = True
        print("Операции отфильтрованы по статусу 'CANCELED'")
        filtered_data_by_state = filter_by_state(transaction_data, "CANCELED")
    elif user_status_choice.upper() == "PENDING":
        norm_user_choice = True
        print("Операции отфильтрованы по статусу 'PENDING'")
        filtered_data_by_state = filter_by_state(transaction_data, "PENDING")
    else:
        print(f'Статус операции "{user_status_choice}" недоступен.')

selection = filtered_data_by_state.copy()
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
                selection = sort_by_date(filtered_data_by_state, False)
            elif date_sort_order == "по убыванию":
                norm_user_choice_order = True
                selection = sort_by_date(filtered_data_by_state, True)
            else:
                print("Такого варианта нет. Введите: 'по возрастанию' или 'по убыванию'\n")
    elif date_sort_flag == "нет":
        norm_user_choice = True
    else:
        print("Такого варианта нет. Введите 'Да' или 'Нет'.")

norm_user_choice = False
while not norm_user_choice:
    rub_transactions = input("Выводить только рублевые транзакции? Да/Нет\n").lower()
    if rub_transactions == "да":
        norm_user_choice = True
        selection = list(filter_by_currency(selection, "RUB"))
    elif rub_transactions == "нет":
        norm_user_choice = True
    else:
        print("Такого варианта нет. Введите 'Да' или 'Нет'.")

norm_user_choice = False
while not norm_user_choice:
    filter_by_word = input("Отфильтровать список транзакций по определённому слову в описании? Да/Нет\n").lower()
    if filter_by_word == "да":
        norm_user_choice = True
        word = input("Введите слово для поиска\n")
        selection = process_bank_search(selection, word)
    elif filter_by_word == "нет":
        norm_user_choice = True
    else:
        print("Такого варианта нет. Введите 'Да' или 'Нет'.")

print("Распечатываю итоговый список транзакций...")
len_selection = len(selection)
print(f"Всего банковских операций в выборке: {len_selection}\n")
if len_selection > 0:
    for transaction in selection:
        if user_file_choice == 1:
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
