import logging

from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import QDialog

from DataStract.WordTest import WordTest
from Models.EditWordModel import EditWordModel
from Views.TestResultDialog import Ui_Dialog


class TestResultModel(Ui_Dialog, QDialog):
    def __init__(self, data: WordTest, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.show()

        self.data: WordTest = data

        self.init()
        self.event_connect()

    def init(self):
        self.listWidget.addItems(self.data.get_wrong_words())
        cursor = self.textBrowser.textCursor()
        cursor.select(QTextCursor.Document)
        char_format = cursor.charFormat()
        cursor.removeSelectedText()
        cursor.insertText(self.data.get_correct_percentage(), char_format)

    def event_connect(self):
        ...
