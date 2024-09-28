from Functions.CSV import open_csv


class WordGroup:
    def __init__(self, group_name: str):
        self._word_data = open_csv(f'./data/words/{group_name}.csv')

    def _add_word(self, word: str, **word_data):
        new_word = self.__create_word(word, **word_data)
        self._word_data.append(new_word)

    def _get_all_words(self):
        words = []
        for data in self._word_data:
            words.append(data['word'])
        return words

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
