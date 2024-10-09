import logging
import random
import time

from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import QDialog

from DataStract.WordGroup import WordGroup
from DataStract.WordTest import WordTest
from Views.TestWordDialog import Ui_Dialog


class TestWordModel(Ui_Dialog, QDialog):
    def __init__(self, word_test: WordTest, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.show()

        self.dictionary = word_test.get_word_group().get_meaning_dict()
        self.begin_time = time.time()
        self.words = list(self.dictionary.keys())
        self.word = ""

        self.init()
        self.event_connect()

    def init(self):
        self.setWindowTitle(f"Test {self.group.get_group_name()}")
        self.next_word()

    def event_connect(self):
        self.radioButton_1.clicked.connect(lambda: self.select_answer(self.radioButton_1.text()))
        self.radioButton_2.clicked.connect(lambda: self.select_answer(self.radioButton_2.text()))
        self.radioButton_3.clicked.connect(lambda: self.select_answer(self.radioButton_3.text()))
        self.radioButton_4.clicked.connect(lambda: self.select_answer(self.radioButton_4.text()))

    def next_word(self):
        self.word = random.choice(self.words)
        self.words.remove(self.word)
        cursor = self.textBrowser.textCursor()
        cursor.select(QTextCursor.Document)
        char_format = cursor.charFormat()
        cursor.removeSelectedText()
        cursor.insertText(self.word, char_format)

        values = list(self.dictionary.values())
        values.remove(self.dictionary[self.word])
        meanings = random.choices(values, k=3)
        answers = []
        for meaning in meanings:
            answers.append(meaning)
        answers.append(self.dictionary[self.word])
        random.shuffle(answers)
        self.radioButton_1.setText(answers[0])
        self.radioButton_2.setText(answers[1])
        self.radioButton_3.setText(answers[2])
        self.radioButton_4.setText(answers[3])

    def select_answer(self, answer: str):
        if answer in self.dictionary[self.word]:
            self.marks[self.word] = True
        else:
            self.marks[self.word] = answer

        if self.words:
            self.radioButton_1.setCheckable(False)
            self.radioButton_2.setCheckable(False)
            self.radioButton_3.setCheckable(False)
            self.radioButton_4.setCheckable(False)
            self.textBrowser.setFocus()
            self.next_word()
        else:
            self.accept()

    def exec_(self):
        is_accept = super().exec_()
        if is_accept:
            return self.marks
        else:
            return is_accept
