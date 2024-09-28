from PySide6.QtCore import Qt, QStringListModel
from PySide6.QtWidgets import QInputDialog, QMessageBox
from Functions.WordGroup import *


class WordBlock:
    def __init__(self, ui):
        self.ui = ui

        self.word_group_model = QStringListModel()
        self.ui.word_group_listView.setModel(self.word_group_model)
        self.word_group_select = ""

    def event_connect(self):
        self.ui.word_group_new_action.triggered.connect(self.word_group_new)
        self.ui.word_group_delete_action.triggered.connect(self.word_group_delete)
        self.ui.word_group_rename_action.triggered.connect(self.word_group_rename)
        self.word_group_model.dataChanged.connect(self.word_group_changed)
        self.ui.word_group_listView.clicked.connect(self.word_group_clicked)

    def init(self):
        self.word_group_update()

    def word_group_update(self):
        self.word_group_model.setStringList(get_all_group())
        self.word_group_select = ""

    def word_group_new(self):
        while True:
            name, ok = QInputDialog.getText(self.ui, "New group", "Enter the name:")
            if ok:
                if name:
                    new_group(name)
                    break
                else:
                    QMessageBox.warning(self.ui, "Warning", "Please enter the name")
            else:
                break
        self.word_group_update()

    def word_group_delete(self):
        if self.word_group_select:
            delete_group(self.word_group_select)
            self.word_group_update()

    def word_group_rename(self):
        selected_index = self.ui.word_group_listView.selectedIndexes()[0]
        self.ui.word_group_listView.edit(selected_index)

    def word_group_changed(self, top_left, bottom_right, roles):
        if self.word_group_select:
            if Qt.EditRole in roles:
                new_name = self.word_group_model.data(top_left, Qt.EditRole)
                rename_group(self.word_group_select, new_name)
            self.word_group_update()

    def word_group_clicked(self, index):
        self.word_group_select = self.word_group_model.data(index, 0)