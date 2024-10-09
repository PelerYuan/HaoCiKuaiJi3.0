import json
import logging
import os

from DataStract.WordGroup import WordGroup
from DataStract.WordTest import WordTest
from Functions.CSV import write_csv
from Functions.JSON import write_json, open_json
from Functions.WordGroup import open_word_group


def new_word_test(name: str, word_group: WordGroup):
    name = check_name(name)
    with open(f'./data/test/{name}.json', 'w', newline='') as file:
        return WordTest(name, word_group)

def open_word_test(name: str):
    data = open_json(f'./data/test/{name}.json')
    data['word_group'] = open_word_group(data['word_group'])
    return WordTest(name, **data)


def save_word_test(name: str, word_test: WordTest):
    write_json(f'./data/test/{name}.json', word_test.get_all_data())


def get_all_test():
    tests = []
    for group in os.listdir('./data/test'):
        tests.append(group.replace('.json', ''))
    return tests


def check_name(test_name):
    while test_name in get_all_test():
        test_name += '_'
    return test_name
