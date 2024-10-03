import time
import unittest

from Functions.JSON import write_json, open_json


class WordMemorize:
    def __init__(self, group_name: str):
        self.__group_name = group_name
        self.__data = open_json(f'./data/memorize/{group_name}.json')

        self.__index = open_json('./data/memorize/index.json')

    def set_data(self, value: dict):
        for key in value.keys():
            self.__data[key] = self.__data.get(key, 1) + value[key]

    def get_data(self):
        return self.__data

    def save_data(self):
        write_json(f'./data/memorize/{self.__group_name}.json', self.__data)
        self.__index[self.__group_name]['last_time'] = time.time()
        write_json('./data/memorize/index.json', self.__index)
