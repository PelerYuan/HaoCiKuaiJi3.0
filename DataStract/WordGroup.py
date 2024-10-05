import logging

from Functions.CSV import open_csv, write_csv


class WordGroup:
    def __init__(self, group_name):
        self.__group_name = group_name
        self.__word_data = {}

    def add_word(self, word: str, part: str = "", meaning: str = "", example: str = "", symbol: str = "",
                 audio: str = ""):
        new_word = {
            'part': part,
            'meaning': meaning,
            'example': example,
            'symbol': symbol,
            'audio': audio
        }
        self.__word_data[word] = new_word

    def delete_word(self, word: str):
        del self.__word_data[word]

    def update_word(self, word: str, part: str = "", meaning: str = "", example: str = "", symbol: str = "",
                    audio: str = ""):
        self.add_word(word, part, meaning, example, symbol, audio)

    def get_word(self, word:str):
        return self.__word_data[word]

    def get_all_data(self):
        return self.__word_data

    def get_meaning_dict(self):
        dictionary = {}
        for word, value in self.__word_data.items():
            dictionary[word] = value['meaning'].replace('\n', ';;')
        return dictionary

    def get_example_dict(self):
        dictionary = {}
        for word, value in self.__word_data.items():
            dictionary[word] = value['example']
        return dictionary

    def get_group_name(self):
        return self.__group_name
