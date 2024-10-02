import logging
import os

from DataStract.WordGroup import WordGroup
from Functions.CSV import open_csv, write_csv


def get_all_group():
    groups = []
    for group in os.listdir('./data/words'):
        groups.append(group.replace('.csv', ''))
    return groups


def delete_group(group_name):
    try:
        os.remove(f'./data/words/{group_name}.csv')
    except FileNotFoundError as e:
        logging.log(logging.ERROR, e)


def rename_group(old_group_name, new_group_name):
    new_group_name = check_name(new_group_name)
    try:
        os.rename(f'./data/words/{old_group_name}.csv', f'./data/words/{new_group_name}.csv')
    except FileNotFoundError as e:
        logging.log(logging.ERROR, e)


def new_group(group_name):
    group_name = check_name(group_name)
    with open(f'./data/words/{group_name}.csv', 'w', newline='') as file:
        group = WordGroup(group_name)


def import_old_group(path: str, name: str):
    csv_file = open_csv(path)
    for word in csv_file:
        word['part'] = word['part_of_speech']
        word['symbol'] = word['phonetic_symbol']
        word['audio'] = word['audio_link']
        del word['part_of_speech']
        del word['phonetic_symbol']
        del word['audio_link']

    name = check_name(name)
    write_csv(f'./data/words/{name}.csv', csv_file)


def check_name(group_name):
    while group_name in get_all_group():
        group_name += '_'
    return group_name
