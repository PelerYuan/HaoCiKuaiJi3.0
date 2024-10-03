import time
from datetime import datetime

from PySide6.QtCore import QModelIndex
from PySide6.QtWidgets import QTableWidgetItem, QTableWidget

from DataStract.WordMemorize import WordMemorize
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
        self.ui.memorize_new_listWidget.doubleClicked.connect(self.start_memorize)

    def init(self):
        self.ui.memorize_new_listWidget.addItems(get_all_group())
        init_memorize()

    def start_memorize(self, item:QModelIndex):
        group_name = self.ui.memorize_new_listWidget.item(item.row()).text()
        word_memorize = MemorizeWordModel(WordGroup(group_name))
        result = word_memorize.exec_()
        if result:
            memorize = open_memorize(group_name)
            print(result)
            memorize.set_data(result)
            memorize.save_data()


    def close(self):
        ...
