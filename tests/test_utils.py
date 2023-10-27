import pytest
import json
from src.utils import display_last_operations, checking_the_dictionary
import os

from datetime import datetime
JSONFILE = os.path.join("operations.json")
checking = display_last_operations(JSONFILE)


def test_display_last_operations():
    with open(os.path.join(os.path.dirname(__file__), 'operations.json'), 'r', encoding='utf-8') as file:
        data = json.load(file)
        data_dict = []
        for list_data in data:
            data_dict.append(list_data)

        assert checking == data_dict


def test_checking_the_dictionary():
    info_dict = []
    for check in checking_the_dictionary(checking):
        info_dict.append(check["date"])
        info_dict.append(check["to"])
        info_dict.append(check["description"])
        info_dict.append(check["operationAmount"])
        info_dict.append(check["operationAmount"]["currency"]["name"])
        assert check["state"] in "EXECUTED"
        assert check["state"] not in "CANCELED"
        assert check["date"] in info_dict
        assert check["to"] in info_dict
        try:
            info_dict.append(check["from"])
            assert check["from"] in info_dict
        except KeyError as e:
            assert check["description"] in info_dict
        assert check["operationAmount"] in info_dict
        assert check["operationAmount"]["currency"]["name"] in info_dict

