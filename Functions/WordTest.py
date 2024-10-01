import logging
import os

from DataStract.WordTest import WordTest
from Functions.CSV import write_csv


def new_test_data(result):
    test_name = get_name()
    word_test = WordTest(result)
    write_csv(f'./data/test/{test_name}.csv', word_test.get_data())


def get_all_test():
    tests = []
    for group in os.listdir('./data/test'):
        tests.append(group.replace('.csv', ''))
    return tests


def get_name():
    return str(len(os.listdir(f'./data/test/')))
