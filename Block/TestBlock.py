from Models.TestWordModel import TestWordModel
from Views.MainWindow import Ui_MainWindow
from Functions.WordGroup import *
from Functions.WordTest import *


class TestBlock:
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui

    def event_connect(self):
        self.ui.new_test_commandLinkButton.clicked.connect(self.start_new_test)

    def init(self):
        self.ui.new_test_comboBox.setFocus()
        self.ui.new_test_comboBox.clear()
        for group in get_all_group():
            self.ui.new_test_comboBox.addItem(group)

    def start_new_test(self):
        group_name = self.ui.new_test_comboBox.currentText()
        group = open_group(group_name)
        test_dialog = TestWordModel(group_name, group.get_meaning_dict(), self.ui)
        result = test_dialog.exec_()
        if result:
            print(result)

    def close(self):
        ...
