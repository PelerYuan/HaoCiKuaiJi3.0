import logging

from PySide6.QtWidgets import QDialog

from Views.EditWordDialog import Ui_Dialog


class EditWordModel(Ui_Dialog, QDialog):
    def __init__(self, part: str | bool, word_data: dict, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.show()

        self.part = part
        self.word_data = word_data

        self.init()
        self.event_connect()

    def init(self):
        self.word_lineEdit.setText(self.word_data['word'])
        self.part_lineEdit.setText(self.word_data['part'])
        self.meaning_textEdit.setText(self.word_data['meaning'])
        self.example_textEdit.setText(self.word_data['example'])
        self.symbol_lineEdit.setText(self.word_data['symbol'])
        self.audio_lineEdit.setText(self.word_data['audio'])

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
        ...

    def get_data(self):
        return {
            'word': self.word_lineEdit.text(),
            'part': self.part_lineEdit.text(),
            'meaning': self.meaning_textEdit.toPlainText(),
            'example': self.example_textEdit.toPlainText(),
            'symbol': self.symbol_lineEdit.text(),
            'audio': self.audio_lineEdit.text(),
        }

    def exec_(self):
        is_accept = super().exec_()
        if is_accept:
            return self.get_data()
        else:
            return is_accept
