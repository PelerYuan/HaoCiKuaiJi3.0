import time
import unittest

from DataStract.WordGroup import WordGroup
from Functions.JSON import write_json, open_json


class WordTest:
    def __init__(self, name: str, word_group: WordGroup, time:float, time_spend:float, correct_percentage:float, result:doct ):
        self.__name = name
        self.__word_group = word_group
        self.__time: float = 0
        self.__time_spend: float = 0
        self.__correct_percentage: float = 0
        self.__result: dict = {word: True for word in word_group.get_all_word()}

    def get_all_data(self):
        return {
            'name': self.__name,
            'word_group': self.__word_group.get_group_name(),
            'time': self.__time,
            'time_spend': self.__time_spend,
            'correct_percentage': self.__correct_percentage,
            'result': self.__result
        }