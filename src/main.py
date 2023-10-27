import os

from src.utils import display_last_operations, checking_the_dictionary
from datetime import datetime

JSONFILE = os.path.join("operations.json")

def main():
    display_last = display_last_operations(JSONFILE)
    checking_dictonary = checking_the_dictionary(display_last)
    checking_dictonary.sort(reverse=True, key=lambda x: x["date"])
    revers = reversed(checking_dictonary)


    # Перебор данных и установка даты в правильном порядке
    for display in revers:

        datetime_str = display['date'].split('T')[0]
        datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d').date().strftime('%d.%m.%Y')

        print(f"{datetime_object} {display['description']}")

        # Вывод счетов со скрытыми в виде * значениями
        where_from = display['to'].split(" ")

        try:
            where = display['from'].split(" ")
            if "from" not in where:
                print(f"{where[0]} {where[-1][:4]} {where[-1][4:6]}** **** {where[-1][-4:]} -> {where_from[0]} **{where_from[-1][-4:]}")

        except KeyError as e:
            print(f"{where[0]} {where[-1][:4]} {where[-1][4:6]}** **** {where[-1][-4:]}")
        print(display["operationAmount"]["amount"], display["operationAmount"]["currency"]["name"])

        print()


main()
