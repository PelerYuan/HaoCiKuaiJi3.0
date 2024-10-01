import logging
import random

from PySide6.QtWidgets import QDialog

from Views.TestWordDialog import Ui_Dialog


class TestWordModel(Ui_Dialog, QDialog):
    def __init__(self, group_name: str, dictionary: dict, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.show()

        self.group_name = group_name
        self.dictionary = dictionary

        self.marks = {}

        self.init()
        self.event_connect()

    def init(self):
        self.setWindowTitle(f"Test {self.group_name}")
        self.next_word()

    def event_connect(self):
        ...

    def next_word(self):
        word = random.choice(list(self.dictionary.keys()))
        self.textBrowser.setText(word)

        meanings = random.choices(list(self.dictionary.values()), k=3)
        answers = []
        for meaning in meanings:
            answers.append(meaning[0])
        answers.append(self.dictionary[word][0])
        random.shuffle(answers)
        self.radioButton_1.setText(answers[0])
        self.radioButton_2.setText(answers[1])
        self.radioButton_3.setText(answers[2])
        self.radioButton_4.setText(answers[3])

    def exec_(self):
        is_accept = super().exec_()
        if is_accept:
            return self.marks
        else:
            return is_accept