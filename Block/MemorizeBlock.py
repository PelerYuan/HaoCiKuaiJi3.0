import time
from datetime import datetime

from PySide6.QtCore import QModelIndex
from PySide6.QtWidgets import QTableWidgetItem, QTableWidget

from DataStract.WordMemorize import WordMemorize
from Functions.JSON import open_json
from Functions.WordMemorize import init_memorize, open_memorize
from Models.MemorizeWordModel import MemorizeWordModel
from Models.TestResultModel import TestResultModel
from Models.TestWordModel import TestWordModel
from Views.MainWindow import Ui_MainWindow
from Functions.WordGroup import *
from Functions.WordTest import *


class MemorizeBlock:
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui

    def event_connect(self):
        self.ui.memorize_new_listWidget.itemDoubleClicked.connect(self.start_memorize)
        self.ui.memorize_review_listWidget.itemDoubleClicked.connect(self.start_memorize)

    def init(self):
        self.ui.memorize_new_listWidget.clear()
        self.ui.memorize_review_listWidget.clear()

        self.ui.memorize_new_listWidget.addItems(get_all_group())
        init_memorize()
        index = open_json('./data/memorize/index.json')
        index = dict(sorted(index.items(), key=lambda item: item[1]['last_time']))
        count = 0
        for group in index.keys():
            if count <= 5:
                if index[group]['last_time']:
                    self.ui.memorize_review_listWidget.addItem(group)
                    count += 1
            else:
                break

    def start_memorize(self, item):
        group_name = item.text()
        word_memorize = MemorizeWordModel(WordGroup(group_name))
        result = word_memorize.exec_()
        if result:
            memorize = open_memorize(group_name)
            memorize.set_data(result)
            memorize.save_data()
            self.init()


    def close(self):
        ...
