import time
from datetime import datetime

from PySide6.QtWidgets import QTableWidgetItem, QTableWidget

from Models.TestResultModel import TestResultModel
from Models.TestWordModel import TestWordModel
from Views.MainWindow import Ui_MainWindow
from Functions.WordGroup import *
from Functions.WordTest import *


class MemorizeBlock:
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui

    def event_connect(self):
        ...

    def init(self):
        self.ui.memorize_new_listWidget.addItems(get_all_group())

    def close(self):
        ...
