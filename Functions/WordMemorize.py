import json
import logging
import os

from DataStract.WordGroup import WordGroup
from DataStract.WordMemorize import WordMemorize
from DataStract.WordTest import WordTest
from Functions.CSV import write_csv
from Functions.JSON import write_json
from Functions.WordGroup import get_all_word_group


def init_memorize():
    path = './data/memorize/index.json'
    if not os.path.exists(path):
        data = {}
        for key in get_all_word_group():
            data[key] = {
                "last_time": None
            }
        write_json(path, data)


def open_memorize(group_name: str):
    with open(f'./data/memorize/{group_name}.json', 'w', newline=''):
        word_memorize = WordMemorize(group_name)
        if not word_memorize.get_data():
            print('aaaaa')
            data = {word['word']: 1 for word in WordGroup(group_name).get_all_data()}
            word_memorize.set_data(data)
            word_memorize.save_data()
        return word_memorize
