from PySide6.QtWidgets import QMainWindow

from Functions.CSV import open_csv, write_csv
from Views.MainWindow import Ui_MainWindow

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, root=None):
        super().__init__(root)
        self.setupUi(self)
        self.show()