import time
from datetime import datetime

from PySide6.QtWidgets import QTableWidgetItem, QTableWidget, QMessageBox

from Models.TestResultModel import TestResultModel
from Models.TestWordModel import TestWordModel
from Views.MainWindow import Ui_MainWindow
from Functions.WordGroup import *
from Functions.WordTest import *


class TestBlock:
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui

    def event_connect(self):
        self.ui.test_new_commandLinkButton.clicked.connect(self.start_new_test)
        self.ui.toolBox.currentChanged.connect(self.init)
        self.ui.test_history_tableWidget.cellDoubleClicked.connect(self.show_test_result)

    def init(self):
        self.ui.test_history_tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.ui.test_history_tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.test_new_lineEdit.clear()
        self.ui.test_new_comboBox.setFocus()
        self.ui.test_new_comboBox.clear()
        for group in get_all_word_group():
            self.ui.test_new_comboBox.addItem(group)
        self.load_test_history()

    def start_new_test(self):
        group_name = self.ui.test_new_comboBox.currentText()
        group = WordGroup(group_name)
        if len(group.get_all_data()) > 5:
            name = self.ui.test_new_lineEdit.text()
            begin_time = time.time()
            if name:
                test_dialog = TestWordModel(group, self.ui)
                result = test_dialog.exec_()
                if result:
                    finish_time = time.time()
                    word_test = new_test(name, group_name, str(datetime.fromtimestamp(begin_time)).split('.')[0],
                                         f"{finish_time - begin_time:.2f} s", result)
                    test_result_dialog = TestResultModel(word_test, self.ui)
                    test_result_dialog.exec_()
        else:
            QMessageBox.warning(self.ui, "Warning", "Please make sure you have more than five words in the group.")

    def show_test_result(self, row, column):
        item = self.ui.test_history_tableWidget.item(row, 1)
        test_result_dialog = TestResultModel(WordTest(item.text()), self.ui)
        test_result_dialog.exec_()

    def load_test_history(self):
        self.ui.test_history_tableWidget.setRowCount(0)
        self.ui.test_history_tableWidget.clearContents()
        for test in get_all_test():
            word_test_data = WordTest(test).get_data()
            row_count = self.ui.test_history_tableWidget.rowCount()
            self.ui.test_history_tableWidget.insertRow(row_count)
            self.ui.test_history_tableWidget.setItem(row_count, 0, QTableWidgetItem(word_test_data['group_name']))
            self.ui.test_history_tableWidget.setItem(row_count, 1, QTableWidgetItem(word_test_data['name']))
            self.ui.test_history_tableWidget.setItem(row_count, 2, QTableWidgetItem(word_test_data['time_spend']))
            self.ui.test_history_tableWidget.setItem(row_count, 3,
                                                     QTableWidgetItem(word_test_data['correct percentage']))
            self.ui.test_history_tableWidget.setItem(row_count, 4, QTableWidgetItem(word_test_data['time']))

    def close(self):
        ...
