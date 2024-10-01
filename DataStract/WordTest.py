import unittest


class WordTest:
    def __init__(self, result):
        self.__result = result

    def get_data(self):
        data = []
        for key in self.__result:
            data.append({
                'word': key,
                'value': self.__result[key]
            })
        return data

    def get_correct_percentage(self):
        count = 0
        for key in self.__result.keys():
            if self.__result[key] is not True:
                count += 1
        return f"{(len(self.__result.keys())-count)/len(self.__result.keys()) * 100:.2f}%"

    def get_wrong_words(self):
        words = []
        for key in self.__result.keys():
            if self.__result[key] is not True:
                words.append(key)
        return words
