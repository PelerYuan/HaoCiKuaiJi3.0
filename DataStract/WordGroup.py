import logging

from DataStract.WordData import WordData
from Functions.CSV import open_csv, write_csv


class WordGroup:
    def __init__(self, group_name):
        self.__group_name = group_name
        self.__word_data:dict[str, WordData] = {}

    def add_word(self, word: WordData) -> None:
        self.__word_data[word.get_word()] = word

    def delete_word(self, word: str) -> None:
        del self.__word_data[word]

    def update_word(self, word:WordData) -> None:
        self.add_word(word)

    def get_word(self, word: str) -> WordData:
        return self.__word_data[word]

    def get_all_data(self) -> dict[str, WordData]:
        return self.__word_data

    def get_meaning_dict(self) -> dict[str, str]:
        dictionary = {}
        for word, value in self.__word_data.items():
            dictionary[word] = value['meaning'].replace('\n', ';;')
        return dictionary

    def get_example_dict(self) -> dict[str, str]:
        dictionary = {}
        for word, value in self.__word_data.items():
            dictionary[word] = value['example']
        return dictionary

    def get_group_name(self) -> str:
        return self.__group_name
