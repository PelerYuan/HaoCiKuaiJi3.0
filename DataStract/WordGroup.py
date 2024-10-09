import logging

from Functions.CSV import open_csv, write_csv


class WordGroup:
    def __init__(self, group_name):
        self.__group_name = group_name
        self.__word_data = {}

    def add_word(self, word: str, part: str = "", meaning: str = "", example: str = "", symbol: str = "",
                 audio: str = "") -> None:
        new_word = {
            'part': part,
            'meaning': meaning,
            'example': example,
            'symbol': symbol,
            'audio': audio
        }
        # del self.__word_data
        self.__word_data[word] = new_word
        print(self.__word_data[word].get('word',0))

    def delete_word(self, word: str) -> None:
        del self.__word_data[word]

    def update_word(self, word: str, part: str = "", meaning: str = "", example: str = "", symbol: str = "",
                    audio: str = "") -> None:
        self.add_word(word, part, meaning, example, symbol, audio)

    def get_word_data(self, word: str) -> dict[str, str]:
        return self.__word_data[word]

    def get_all_data(self) -> dict[str, dict]:
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
