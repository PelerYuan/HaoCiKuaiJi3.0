import logging

from Functions.CSV import open_csv, write_csv


class WordGroup:
    def __init__(self, group_name: str):
        self.__group_name = group_name
        self.file_path = f'./data/words/{group_name}.csv'
        self.__word_data = open_csv(self.file_path)

    def add_word(self, word: str, **word_data):
        new_word = self.__create_word(word, **word_data)
        self.__word_data.append(new_word)

    def delete_word(self, index: int):
        del self.__word_data[index]

    def edit_word(self, index: int, **word_data):
        word = self.__create_word(**word_data)
        self.__word_data[index] = word

    def update_word(self, word_: str, **word_data):
        print(word_)
        print(word_data)
        for i in range(len(self.__word_data)):
            if self.__word_data[i]['word'] == word_:
                self.__word_data[i] = word_data
                return
        logging.log(logging.ERROR, f'Word not found: {word_}')

    def get_word(self, index: int):
        return self.__word_data[index]

    def get_all_word(self):
        return self.__word_data

    def get_meaning_dict(self):
        dictionary = {}
        for word in self.__word_data:
            dictionary[word['word']] = word['meaning'].replace('\n', ';;')
        return dictionary

    def get_group_name(self):
        return self.__group_name

    def save_data(self):
        write_csv(self.file_path, self.__word_data)

    def __create_word(self, word: str, part: str = "", meaning: str = "", example: str = "", symbol: str = "",
                      audio: str = ""):
        return {
            'word': word,
            'part': part,
            'meaning': meaning,
            'example': example,
            'symbol': symbol,
            'audio': audio
        }
