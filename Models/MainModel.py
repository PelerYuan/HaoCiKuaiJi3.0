from PySide6.QtCore import QStringListModel, Qt
from PySide6.QtWidgets import QMainWindow, QInputDialog, QMessageBox, QTableView

from Block.WordBlock import WordBlock
from Functions.WordGroup import *
from Views.MainWindow import Ui_MainWindow

class MainModel(Ui_MainWindow, QMainWindow):
    def __init__(self, root=None):
        super().__init__(root)
        self.setupUi(self)
        self.show()

        self.word_block = WordBlock(self)

        self.init()
        self.event_connect()

    def init(self):
        self.word_block.init()
        self.word_tableView.setSelectionBehavior(QTableView.SelectRows)  # 选择整行
        self.word_tableView.resizeColumnsToContents()

    def event_connect(self):
        self.word_block.event_connect()
