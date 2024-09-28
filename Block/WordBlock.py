from PySide6.QtCore import Qt, QStringListModel
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QInputDialog, QMessageBox, QTableView
from Functions.WordGroup import *
from Views.MainWindow import Ui_MainWindow


class WordBlock:
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui

        self.word_group_model = QStringListModel()
        self.ui.word_group_listView.setModel(self.word_group_model)
        self.word_group_select = ""

        self.word_model = QStandardItemModel(0, 0)
        self.word_model.clear()
        self.word_model.setHorizontalHeaderLabels(['word', 'part', 'meaning', 'example', 'symbol', 'audio'])
        self.ui.word_tableView.setModel(self.word_model)

        self.word_group: None | WordGroup = None

    def event_connect(self):
        self.ui.word_group_new_action.triggered.connect(self.word_group_new)
        self.ui.word_group_delete_action.triggered.connect(self.word_group_delete)
        self.ui.word_group_rename_action.triggered.connect(self.word_group_rename)
        self.word_group_model.dataChanged.connect(self.word_group_changed)
        self.ui.word_group_listView.clicked.connect(self.word_group_clicked)
        self.ui.word_new_pushButton.clicked.connect(self.word_new)
        self.ui.word_delete_pushButton.clicked.connect(self.word_delete)

    def init(self):
        self.word_group_update()
        self.ui.word_tableView.setSelectionBehavior(QTableView.SelectRows)
        self.ui.word_tableView.resizeColumnsToContents()

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
        self.word_group = WordGroup(self.word_group_select)
        self.word_update()

    def word_update(self):
        if self.word_group.get_all_word():
            self.word_group.save_data()
        self.word_model.clear()
        self.word_model.setHorizontalHeaderLabels(['word', 'part', 'meaning', 'example', 'symbol', 'audio'])
        for word in self.word_group.get_all_word():
            row_data = []
            for key in word.keys():
                row_data.append(QStandardItem(word[key]))
            self.word_model.appendRow(row_data)

    def word_new(self):
        while True:
            word, ok = QInputDialog.getText(self.ui, "New word", "Enter the word:")
            if ok:
                if word:
                    self.word_group.add_word(word)
                    break
                else:
                    QMessageBox.warning(self.ui, "Warning", "Please enter the word")
            else:
                break
        self.word_update()

    def word_delete(self):
        selected_indexes = self.ui.word_tableView.selectionModel().selectedIndexes()
        if selected_indexes:
            selected_rows = sorted(set(index.row() for index in selected_indexes))
            for i in range(len(selected_rows)):
                self.word_group.delete_word(selected_rows[i] - i)
        self.word_update()

    