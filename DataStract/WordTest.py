import unittest

from Functions.JSON import write_json, open_json


class WordTest:
    def __init__(self, name: str):
        self.__name = name
        self.file_path = f'./data/test/{name}.json'
        self.__data = open_json(self.file_path)
        if self.__data:
            self.__result = self.__data['result']
        else:
            self.__result = {}

    def set_data(self, group_name: str, time: str, time_spend: str, result: dict):
        self.__result = result
        self.__data = {
            'name': self.__name,
            'group_name': group_name,
            'time': time,
            'time_spend': time_spend,
            'correct percentage': self.__get_correct_percentage(),
            'result': result
        }

    def get_data(self):
        return self.__data

    def save_data(self):
        write_json(self.file_path, self.__data)

    def get_wrong_words(self):
        words = []
        for key in self.__result.keys():
            if self.__result[key] is not True:
                words.append(key)
        return words

    def get_correct_percentage(self):
        return float(self.__data['correct percentage'][:-1]) / 100

    def __get_correct_percentage(self):
        count = 0
        for key in self.__result.keys():
            if self.__result[key] is not True:
                count += 1
        return f"{(len(self.__result.keys()) - count) / len(self.__result.keys()) * 100:.2f}%"
