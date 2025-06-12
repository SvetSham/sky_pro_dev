print("""Привет! Добро пожаловать в программу работы
с банковскими транзакциями.""")
norm_user_choice = False
while not norm_user_choice:
    user_file_choice = int(input(("""Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
""")))
    if user_file_choice == 1:
        norm_user_choice = True
        print("Для обработки выбран JSON-файл")

    elif user_file_choice == 2:
        norm_user_choice = True
        print("Для обработки выбран CSV-файл")

    elif user_file_choice == 3:
        norm_user_choice = True
        print("Для обработки выбран XLSX-файл")
    else:
        print("Нет такого варианта. Попробуйте ещё раз.")

norm_user_choice = False
while not norm_user_choice:
    user_status_choice = input("""Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
""")
    if user_status_choice.upper() == "EXECUTED":
        norm_user_choice = True
        print("Операции отфильтрованы по статусу 'EXECUTED'")

    elif user_status_choice.upper() == "CANCELED":
        norm_user_choice = True
        print("Операции отфильтрованы по статусу 'CANCELED'")

    elif user_status_choice.upper() == "PENDING":
        norm_user_choice = True
        print("Операции отфильтрованы по статусу 'PENDING'")

    else:
        print(f'Статус операции "{user_status_choice}" недоступен.')


