import json
import os

JSONFILE = "operations.json"


def display_last_operations(file):
    """
    Считывает данные из файла
    """
    # Чтение данных из файла операций
    file_path = os.path.join(os.path.dirname(__file__), file)
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        data_dict = []
        for list_data in data:
            data_dict.append(list_data)
        return data_dict


display_last = display_last_operations(JSONFILE)


def checking_the_dictionary(value):
    """
    Выводит последние 5 записей
    """
    executed = []
    count = 0
    for item in value[::-1]:
        if count == 5:
            break
        if "EXECUTED" in item.values() \
                and "from" in item.keys():
            executed.append(item)
            count += 1
        elif "EXECUTED" in item.values() \
                and "to" in item.keys():
            executed.append(item)
            count += 1
    return executed



