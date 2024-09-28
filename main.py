import sys

from PySide6.QtCore import QFile
from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet
from Models.MainModel import MainModel


if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_blue.xml')
    main_window = MainModel()
    sys.exit(app.exec())