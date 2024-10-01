import logging

from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import QDialog

from Models.EditWordModel import EditWordModel
from Views.TestResultDialog import Ui_Dialog


class TestResultModel(Ui_Dialog, QDialog):
    def __init__(self, result: dict, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.show()

        self.result: dict = result

        self.init()
        self.event_connect()

    def init(self):
        count = 0
        for key in self.result.keys():
            if self.result[key] is not True:
                self.listWidget.addItem(key)
                count += 1
        cursor = self.textBrowser.textCursor()
        cursor.select(QTextCursor.Document)
        char_format = cursor.charFormat()
        cursor.removeSelectedText()
        percentage = f"{(len(self.result.keys())-count)/len(self.result.keys()) * 100:.2f}%"
        cursor.insertText(percentage, char_format)

    def event_connect(self):
        ...
