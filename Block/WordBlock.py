from PySide6.QtCore import Qt, QStringListModel, QModelIndex, QUrl
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtWidgets import QInputDialog, QMessageBox, QTableView, QTableWidget, QTableWidgetItem, QPushButton, \
    QFileDialog
import pygame

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
        self.word_group_select = ""

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

    def init(self):
        self.word_group_update()
        self.ui.word_tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.ui.word_tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

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

    def word_group_refresh(self):
        if self.word_group:
            self.word_update()

    def word_group_update_data(self):
        if self.word_group:
            for word in self.word_group.get_all_word():
                self.word_search_thread.add_word(word['word'])

    def word_group_import_2v(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self.ui, "Open old group file", "", "HaoCiKuaiJi2.0 (*.csv)",
                                                   options=options)
        if file_name:
            while True:
                name, ok = QInputDialog.getText(self.ui, "Import group", "Enter the group name:")
                if ok:
                    if name:
                        import_old_group(file_name, name)
                        break
                    else:
                        QMessageBox.warning(self.ui, "Warning", "Please enter the name")
                else:
                    break
            self.word_group_update()
            for word in WordGroup(name).get_all_word():
                self.word_search_thread.add_word(word['word'])

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
        self.ui.word_tableWidget.setRowCount(0)
        self.ui.word_tableWidget.clearContents()
        for word in self.word_group.get_all_word():
            self.word_insert(word)

    def word_insert(self, word_data: dict):
        row_count = self.ui.word_tableWidget.rowCount()
        self.ui.word_tableWidget.insertRow(row_count)
        self.ui.word_tableWidget.setItem(row_count, 0, QTableWidgetItem(word_data['word']))
        self.ui.word_tableWidget.setItem(row_count, 1, QTableWidgetItem(word_data['part']))
        self.ui.word_tableWidget.setItem(row_count, 2, QTableWidgetItem(word_data['meaning']))
        self.ui.word_tableWidget.setItem(row_count, 3, QTableWidgetItem(word_data['example']))

        play_button = QPushButton(f"Play {word_data['symbol']}", self.ui)
        play_button.clicked.connect(lambda: self.word_play_audio(word_data['word']))
        self.ui.word_tableWidget.setCellWidget(row_count, 4, play_button)

    def word_new(self):
        while True:
            word, ok = QInputDialog.getText(self.ui, "New word", "Enter the word:")
            if ok:
                if word:
                    self.word_group.add_word(word)
                    self.word_search_thread.add_word(word)
                    break
                else:
                    QMessageBox.warning(self.ui, "Warning", "Please enter the word")
            else:
                break
        self.word_group.save_data()
        self.word_update()

    def word_delete(self):
        selected_indexes = self.ui.word_tableWidget.selectionModel().selectedIndexes()
        if selected_indexes:
            selected_rows = sorted(set(index.row() for index in selected_indexes))
            for i in range(len(selected_rows)):
                self.word_group.delete_word(selected_rows[i] - i)
        self.word_group.save_data()
        self.word_update()

    def word_edit(self, part: str | bool = False):
        selected_indexes = self.ui.word_tableWidget.selectionModel().selectedIndexes()
        if selected_indexes:
            row = selected_indexes[0].row()
            edit_word_dialog = EditWordModel(part, self.word_group.get_word(row), self.ui)
            result = edit_word_dialog.exec_()
            if result:
                self.word_group.edit_word(row, **result)
        self.word_group.save_data()
        self.word_update()

    def word_double_clicked(self, index: QModelIndex):
        column = index.column()
        self.word_edit(['word', 'part', 'meaning', 'example', 'symbol', 'audio'][column])

    def word_search_finished(self, data: dict):
        self.word_group.update_word(data['word'], **data)
        self.word_group.save_data()
        self.word_update()

    def word_play_audio(self, word: str):
        pygame.mixer.music.load(f'./data/audio/{word}.mp3')
        pygame.mixer.music.play()

    def close(self):
        self.word_search_thread.stop()
        self.word_search_thread.wait()
