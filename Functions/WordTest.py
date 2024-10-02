import json
import logging
import os

from DataStract.WordTest import WordTest
from Functions.CSV import write_csv


def new_test(name: str, group_name: str, time: str, time_spend: str, result: dict):
    name = check_name(name)
    with open(f'./data/test/{name}.json', 'w', newline='') as file:
        word_test = WordTest(name)
        word_test.set_data(group_name, time, time_spend, result)
        word_test.save_data()
        return word_test


def get_all_test():
    tests = []
    for group in os.listdir('./data/test'):
        tests.append(group.replace('.json', ''))
    return tests


def check_name(test_name):
    while test_name in get_all_test():
        test_name += '_'
    return test_name
