import logging

import pygame
from PySide6.QtWidgets import QDialog

from DataStract.WordData import WordData
from Views.EditWordDialog import Ui_Dialog


class EditWordModel(Ui_Dialog, QDialog):
    def __init__(self, part: str | bool, word: WordData, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.show()

        self.part = part
        self.word = word

        self.init()
        self.event_connect()

    def init(self):
        self.word_lineEdit.setText(self.word.get_word())
        self.part_lineEdit.setText(self.word.get_part())
        self.meaning_textEdit.setText(self.word.get_word())
        self.example_textEdit.setText(self.word.get_example())
        self.symbol_lineEdit.setText(self.word.get_symbol())
        self.audio_lineEdit.setText(self.word.get_audio())

        if self.part == "word":
            self.tabWidget.setCurrentIndex(0)
            self.word_lineEdit.setFocus()
        elif self.part == "part":
            self.tabWidget.setCurrentIndex(0)
            self.part_lineEdit.setFocus()
        elif self.part == "symbol":
            self.tabWidget.setCurrentIndex(0)
            self.symbol_lineEdit.setFocus()
        elif self.part == "meaning":
            self.tabWidget.setCurrentIndex(1)
            self.meaning_textEdit.setFocus()
        elif self.part == "example":
            self.tabWidget.setCurrentIndex(2)
            self.example_textEdit.setFocus()
        elif self.part == "audio":
            self.tabWidget.setCurrentIndex(3)
            self.audio_lineEdit.setFocus()
        elif self.part is False:
            ...
        else:
            logging.log(logging.ERROR, f"Unknown option for word edit: {self.part}")

    def event_connect(self):
        self.audio_test_pushButton.clicked.connect(self.word_play_audio)

    def get_data(self):
        return WordData(
            word=self.word.get_word(),
            part=self.part_lineEdit.text(),
            meaning=self.meaning_textEdit.toPlainText(),
            example=self.example_textEdit.toPlainText(),
            symbol=self.symbol_lineEdit.text(),
            audio=self.audio_lineEdit.text(),
        )

    def word_play_audio(self):
        pygame.mixer.music.load(f'./data/audio/{self.word.get_word()}.mp3')
        pygame.mixer.music.play()

    def exec_(self):
        is_accept = super().exec_()
        if is_accept:
            return self.get_data()
        else:
            return is_accept
