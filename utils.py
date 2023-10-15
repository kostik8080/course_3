import json
import pprint
from datetime import date


def display_last_operations():
    """
    Считывает данные из файла
    """
    # Чтение данных из файла операций
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        data_dict = []
        for list_data in data:
            data_dict.append(list_data)
        return data_dict


display_last = display_last_operations()


def checking_the_dictionary(value):
    """
    Выводит последние 5 записей
    """
    executed = []
    count = 0
    for i in value[::-1]:
        if count == 5:
            break
        if "EXECUTED" in i.values() \
                and "from" in i.keys():
            executed.append(i)
            count += 1
    return executed



