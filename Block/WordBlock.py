from PySide6.QtCore import Qt, QStringListModel, QModelIndex, QUrl
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtWidgets import QInputDialog, QMessageBox, QTableView, QTableWidget, QTableWidgetItem, QPushButton, \
    QFileDialog
import pygame

from DataStract.ConstData import ConstData
from DataStract.WordData import WordData
from Functions.WordGroup import *
from Models.EditWordModel import EditWordModel
from Thread.WordSearchThread import WordSearchThread
from Views import EditWordDialog
from Views.MainWindow import Ui_MainWindow


class WordBlock:
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui

        self.word_group_model = QStringListModel()
        self.ui.word_group_listView.setModel(self.word_group_model)

        self.word_search_thread = WordSearchThread()
        self.word_search_thread.task_finished.connect(self.word_search_finished)
        self.word_search_thread.start()

        self.word_group: None | WordGroup = None

        pygame.init()
        pygame.mixer.init()

    def event_connect(self):
        self.ui.word_group_new_action.triggered.connect(self.word_group_new)
        self.ui.word_group_delete_action.triggered.connect(self.word_group_delete)
        self.ui.word_group_rename_action.triggered.connect(self.word_group_rename)
        self.ui.word_group_refresh_action.triggered.connect(self.word_group_refresh)
        self.ui.word_group_update_data_action.triggered.connect(self.word_group_update_data)
        self.ui.word_group_import_2v_action.triggered.connect(self.word_group_import_2v)
        self.word_group_model.dataChanged.connect(self.word_group_changed)
        self.ui.word_group_listView.clicked.connect(self.word_group_clicked)
        self.ui.word_new_pushButton.clicked.connect(self.word_new)
        self.ui.word_delete_pushButton.clicked.connect(self.word_delete)
        self.ui.word_tableWidget.doubleClicked.connect(self.word_double_clicked)
        self.ui.word_edit_pushButton.clicked.connect(self.word_edit)
        self.ui.word_search_pushButton.clicked.connect(self.word_search)

    def init(self):
        self.word_group_update()
        self.ui.word_tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.ui.word_tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

    def update(self):
        if self.word_group:
            self.word_update()

    def word_group_update(self):
        if self.word_group:
            save_word_group(self.word_group)
        self.word_group_model.setStringList(get_all_word_group())
        self.word_group = None

    def word_group_new(self):
        while True:
            name, ok = QInputDialog.getText(self.ui, "New group", "Enter the name:")
            if ok:
                if name:
                    new_word_group(name)
                    break
                else:
                    QMessageBox.warning(self.ui, "Warning", "Please enter the name")
            else:
                break
        self.word_group_update()

    def word_group_delete(self):
        if self.word_group:
            delete_word_group(self.word_group.get_group_name())
            self.word_group = None
            self.word_group_update()

    def word_group_rename(self):
        selected_index = self.ui.word_group_listView.selectedIndexes()[0]
        self.ui.word_group_listView.edit(selected_index)

    def word_group_refresh(self):
        if self.word_group:
            self.word_update()

    def word_group_update_data(self):
        if self.word_group:
            for word in self.word_group.get_all_data().keys():
                self.word_search_thread.add_word(word, self.word_group)

    def word_group_import_2v(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self.ui, "Open old group file", "", "HaoCiKuaiJi2.0 (*.csv)",
                                                   options=options)
        if file_path:
            while True:
                name, ok = QInputDialog.getText(self.ui, "Import group", "Enter the group name:")
                if ok:
                    if name:
                        import_old_word_group(file_path, name)
                        break
                    else:
                        QMessageBox.warning(self.ui, "Warning", "Please enter the group name")
                else:
                    break
            self.word_group_update()
            self.word_group_update_data()

    def word_group_changed(self, top_left, bottom_right, roles):
        if self.word_group:
            if Qt.EditRole in roles:
                new_name = self.word_group_model.data(top_left, Qt.EditRole)
                rename_word_group(self.word_group.get_group_name(), new_name)
            self.word_group_update()

    def word_group_clicked(self, index):
        if self.word_group:
            save_word_group(self.word_group)
        self.word_group = open_word_group(self.word_group_model.data(index, 0))
        self.word_update()

    def word_update(self):
        self.ui.word_tableWidget.setRowCount(0)
        self.ui.word_tableWidget.clearContents()
        for word, word_data in self.word_group.get_all_data().items():
            self.word_insert(word, word_data)

    def word_insert(self, word: str, word_data: WordData):
        row_count = self.ui.word_tableWidget.rowCount()
        self.ui.word_tableWidget.insertRow(row_count)
        self.word_update_row(row_count, word_data)

    def word_update_row(self, row_count: int, word_data: WordData):
        self.ui.word_tableWidget.setItem(row_count, 0, QTableWidgetItem(word_data.get_word()))
        self.ui.word_tableWidget.setItem(row_count, 1, QTableWidgetItem(word_data.get_part()))
        self.ui.word_tableWidget.setItem(row_count, 2, QTableWidgetItem(word_data.get_meaning()))
        self.ui.word_tableWidget.setItem(row_count, 3, QTableWidgetItem(word_data.get_example()))

        play_button = QPushButton(f"Play {word_data.get_symbol()}", self.ui)
        play_button.clicked.connect(lambda: self.word_play_audio(word_data.get_word()))
        self.ui.word_tableWidget.setCellWidget(row_count, 4, play_button)

    def word_new(self):
        while True:
            word, ok = QInputDialog.getText(self.ui, "New word", "Enter the word:")
            if ok:
                if word:
                    self.word_group.add_word(WordData(word))
                    break
                else:
                    QMessageBox.warning(self.ui, "Warning", "Please enter the word")
            else:
                break
        self.word_insert(word, self.word_group.get_word(word))

    def word_delete(self):
        selected_indexes = self.ui.word_tableWidget.selectionModel().selectedIndexes()
        if selected_indexes:
            selected_rows = sorted(set(index.row() for index in selected_indexes))
            for i in range(len(selected_rows)):
                self.word_group.delete_word(self.ui.word_tableWidget.item(selected_rows[i] - i, 0).text())
                self.ui.word_tableWidget.removeRow(selected_rows[i] - i)

    def word_search(self):
        selected_indexes = self.ui.word_tableWidget.selectionModel().selectedIndexes()
        if selected_indexes:
            selected_rows = sorted(set(index.row() for index in selected_indexes))
            for row in selected_rows:
                word = self.ui.word_tableWidget.item(row, 0).text()
                self.word_search_thread.add_word(word, self.word_group)
            self.word_search_thread.add_word(ConstData.STOP_SIGN, self.word_group)

    def word_edit(self, part: str | bool = False):
        selected_indexes = self.ui.word_tableWidget.selectionModel().selectedIndexes()
        if selected_indexes:
            row = selected_indexes[0].row()
            word = self.ui.word_tableWidget.item(row, 0).text()
            edit_word_dialog = EditWordModel(part, self.word_group.get_word(word), self.ui)
            result = edit_word_dialog.exec_()
            if result:
                self.word_group.update_word(result)
                self.word_update_row(row, result)

    def word_double_clicked(self, index: QModelIndex):
        column = index.column()
        self.word_edit(['word', 'part', 'meaning', 'example', 'symbol', 'audio'][column])

    def word_search_finished(self, word: WordData, word_group: WordGroup):
        if word.is_stop_sign():
            if word_group is self.word_group:
                self.word_update()

    def word_play_audio(self, word: str):
        pygame.mixer.music.load(f'./data/audio/{word}.mp3')
        pygame.mixer.music.play()

    def close(self):
        if self.word_group:
            save_word_group(self.word_group)
        self.word_search_thread.stop()
        self.word_search_thread.wait()
