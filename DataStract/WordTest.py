import time
import unittest

from DataStract.WordGroup import WordGroup
from Functions.JSON import write_json, open_json


class WordTest:
    def __init__(self, name: str, word_group: WordGroup, ):
        self.__name = name
        self.__word_group = word_group
        self.__time: float = 0
        self.__time_spend: float = 0
        self.__correct_percentage: float = 0
        self.__result: dict = {word: True for word in word_group.get_all_word()}
