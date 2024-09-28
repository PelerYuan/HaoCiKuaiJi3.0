from Functions.CSV import open_csv, write_csv


class WordGroup:
    def __init__(self, group_name: str):
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

    def get_word(self, index: int):
        return self.__word_data[index]

    def get_all_word(self):
        return self.__word_data

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
