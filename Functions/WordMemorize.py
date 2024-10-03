import json
import logging
import os

from DataStract.WordMemorize import WordMemorize
from DataStract.WordTest import WordTest
from Functions.CSV import write_csv
from Functions.JSON import write_json
from Functions.WordGroup import get_all_group


def init_memorize():
    path = './data/memorize/index.json'
    if not os.path.exists(path):
        data = {}
        for key in get_all_group():
            data[key] = {
                "last_time": None
            }
        write_json(path, data)


def new_memorize(group_name: str):
    init_memorize()
    with open(f'./data/memorize/{group_name}.json', 'w', newline=''):
        word_memorize = WordMemorize(group_name)
        return word_memorize
