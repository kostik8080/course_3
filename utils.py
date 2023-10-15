import json
import pprint
from datetime import date


def display_last_operations():
    # Чтение данных из файла операций
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        data_dict = []
        for list_data in data[-5:]:
            data_dict.append(list_data)
        return data_dict



