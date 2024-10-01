from Views.MainWindow import Ui_MainWindow
from Functions.WordGroup import *
from Functions.WordTest import *


class TestBlock:
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui

    def event_connect(self):
        ...

    def init(self):
        self.ui.new_test_comboBox.setFocus()
        for group in get_all_group():
            self.ui.new_test_comboBox.addItem(group)

    def close(self):
        ...
