import logging
import os

from DataStract.WordData import WordData
from DataStract.WordGroup import WordGroup
from Functions.CSV import open_csv, write_csv


def new_word_group(group_name: str) -> WordGroup:
    group_name = check_name(group_name)
    with open(f'./data/words/{group_name}.csv', 'w', newline='') as file:
        return WordGroup(group_name)


def open_word_group(group_name: str) -> WordGroup:
    data = open_csv(f'./data/words/{group_name}.csv')
    group = WordGroup(group_name)
    for value in data:
        group.add_word(WordData(**value))
    return group


def get_all_word_group() -> list[str]:
    groups = []
    for group in os.listdir('./data/words'):
        groups.append(group.replace('.csv', ''))
    return groups


def delete_word_group(group_name: str) -> None:
    os.remove(f'./data/words/{group_name}.csv')


def rename_word_group(old_group_name: str, new_group_name: str) -> None:
    new_group_name = check_name(new_group_name)
    os.rename(f'./data/words/{old_group_name}.csv', f'./data/words/{new_group_name}.csv')

def save_word_group(word_group: WordGroup) -> None:
    data = []
    for word, word_data in word_group.get_all_data().items():
        data.append(word_data.get_all_data())
    write_csv(f'./data/words/{word_group.get_group_name()}.csv', data)


def import_old_word_group(old_group_path: str, new_group_name: str):
    csv_file = open_csv(old_group_path)
    for word in csv_file:
        word['part'] = word['part_of_speech']
        word['symbol'] = word['phonetic_symbol']
        word['audio'] = word['audio_link']
        del word['part_of_speech']
        del word['phonetic_symbol']
        del word['audio_link']

    new_group_name = check_name(new_group_name)
    write_csv(f'./data/words/{new_group_name}.csv', csv_file)


def check_name(group_name):
    while group_name in get_all_word_group():
        group_name += '_'
    return group_name
