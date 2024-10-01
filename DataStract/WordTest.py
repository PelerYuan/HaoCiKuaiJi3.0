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