import logging
import random

from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import QDialog

from DataStract.WordGroup import WordGroup
from DataStract.WordMemorize import WordMemorize
from Functions.WordMemorize import open_memorize
from Views.MemorizeWordDialog import Ui_Dialog


class MemorizeWordModel(Ui_Dialog, QDialog):
    def __init__(self, group: WordGroup, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.show()

        self.group = group
        self.dictionary = group.get_example_dict()

        self.data = open_memorize(group.get_group_name()).get_data()
        self.word = ""
        self.words = list(self.dictionary.keys())
        self.count = 0

        self.init()
        self.event_connect()

    def init(self):
        self.setWindowTitle(f"Memorize {self.group.get_group_name()}")
        self.next_word()

    def event_connect(self):
        self.yes_pushButton.clicked.connect(self.yes)
        self.no_pushButton.clicked.connect(self.no)
        self.tip_pushButton.clicked.connect(self.tip)

    def next_word(self):
        if self.count < len(self.dictionary.keys()) or len(self.words) > 0:
            self.example_textBrowser.clear()
            word = random.choices(list(self.data.keys()), weights=list(self.data.values()), k=1)[0]
            while word == self.word:
                word = random.choices(list(self.data.keys()), weights=list(self.data.values()), k=1)[0]
            self.word = word
            try:
                self.words.remove(word)
            except ValueError:
                ...
            cursor = self.word_textBrowser.textCursor()
            cursor.select(QTextCursor.Document)
            char_format = cursor.charFormat()
            cursor.removeSelectedText()
            cursor.insertText(self.word, char_format)
        else:
            self.accept()

    def yes(self):
        self.count += 1
        data = self.data.get(self.word, 0)
        if data > 1:
            self.data[self.word] -= 1
        self.next_word()

    def no(self):
        self.count -= 1
        self.data[self.word] = self.data.get(self.word, 0) + 1
        self.next_word()

    def tip(self):
        self.example_textBrowser.setText(self.dictionary[self.word])

    def exec_(self):
        is_accept = super().exec_()
        if is_accept:
            return self.data
        else:
            return is_accept
