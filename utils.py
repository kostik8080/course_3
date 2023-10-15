import json
import pprint
from datetime import date


def display_last_operations():
    # Чтение данных из файла операций
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        data_dict = []
        for list_data in data:
            data_dict.append(list_data)
        return data_dict


display_last = display_last_operations()


def checking_the_dictionary(value):
    executed = []
    for i in value[-7:]:
        if "EXECUTED" in i.values() \
                and "from" in i.keys():
            executed.append(i)
    return executed



