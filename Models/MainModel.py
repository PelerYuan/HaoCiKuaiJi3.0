from PySide6.QtCore import QStringListModel, Qt
from PySide6.QtWidgets import QMainWindow, QInputDialog, QMessageBox
from Functions.WordGroup import *
from Views.MainWindow import Ui_MainWindow

class MainModel(Ui_MainWindow, QMainWindow):
    def __init__(self, root=None):
        super().__init__(root)
        self.setupUi(self)
        self.show()

        self.word_group_model = QStringListModel()
        self.word_group_listView.setModel(self.word_group_model)
        self.word_group_select = ""

        self.event_connect()

    def event_connect(self):
        self.init()
        self.word_group_new_action.triggered.connect(self.word_group_new)
        self.word_group_delete_action.triggered.connect(self.word_group_delete)
        self.word_group_rename_action.triggered.connect(self.word_group_rename)
        self.word_group_model.dataChanged.connect(self.word_group_changed)
        self.word_group_listView.clicked.connect(self.word_group_clicked)

    def init(self):
        self.word_group_update()

    def word_group_update(self):
        self.word_group_model.setStringList(get_all_group())
        self.word_group_select = ""

    def word_group_new(self):
        while True:
            name, ok = QInputDialog.getText(self, "New group", "Enter the name:")
            if ok:
                if name:
                    new_group(name)
                    break
                else:
                    QMessageBox.warning(self, "Warning", "Please enter the name")
            else:
                break
        self.word_group_update()


    def word_group_delete(self):
        if self.word_group_select:
            delete_group(self.word_group_select)
            self.word_group_update()

    def word_group_rename(self):
        selected_index = self.word_group_listView.selectedIndexes()[0]
        self.word_group_listView.edit(selected_index)

    def word_group_changed(self, top_left, bottom_right, roles):
        if self.word_group_select:
            if Qt.EditRole in roles:
                new_name = self.word_group_model.data(top_left, Qt.EditRole)
                rename_group(self.word_group_select, new_name)
            self.word_group_update()

    def word_group_clicked(self, index):
        self.word_group_select = self.word_group_model.data(index, 0)