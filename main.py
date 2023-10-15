

from utils import display_last_operations, checking_the_dictionary
from datetime import date

if __name__ == '__main__':
    display_last = display_last_operations()
    checking_dictonary = checking_the_dictionary(display_last)

    for display in checking_dictonary:
        dates = display["date"][:10]
        date_format = date.fromisoformat(dates)
        print(f"{date_format.day}.{date_format.month}.{date_format.year} {display['description']}")
        where_from = display['to'].split(" ")

        try:
            where = display['from'].split(" ")
            if "from" not in where:
                print(f"{where_from[0]} {where_from[1][:4]} {where_from[1][4:6]}** **** {where_from[1][-4:]} -> {where[0]} **{where[1][-4:]}")

        except KeyError as e:
            print(f"{where_from[0]} {where_from[1][:4]} {where_from[1][4:6]}** **** {where_from[1][-4:]}")
        print(display["operationAmount"]["amount"], display["operationAmount"]["currency"]["name"])

        print()

