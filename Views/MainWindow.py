# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QListView, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTableView,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(994, 630)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_4 = QHBoxLayout(self.tab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.word_group_new_pushButton = QPushButton(self.groupBox)
        self.word_group_new_pushButton.setObjectName(u"word_group_new_pushButton")

        self.horizontalLayout_2.addWidget(self.word_group_new_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.word_group_rename_pushButton = QPushButton(self.groupBox)
        self.word_group_rename_pushButton.setObjectName(u"word_group_rename_pushButton")

        self.horizontalLayout_3.addWidget(self.word_group_rename_pushButton)

        self.word_group_delete_pushButton = QPushButton(self.groupBox)
        self.word_group_delete_pushButton.setObjectName(u"word_group_delete_pushButton")

        self.horizontalLayout_3.addWidget(self.word_group_delete_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.word_group_listView = QListView(self.groupBox)
        self.word_group_listView.setObjectName(u"word_group_listView")

        self.verticalLayout.addWidget(self.word_group_listView)


        self.horizontalLayout_4.addWidget(self.groupBox)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.word_new_pushButton = QPushButton(self.tab)
        self.word_new_pushButton.setObjectName(u"word_new_pushButton")

        self.horizontalLayout.addWidget(self.word_new_pushButton)

        self.word_edit_pushButton = QPushButton(self.tab)
        self.word_edit_pushButton.setObjectName(u"word_edit_pushButton")

        self.horizontalLayout.addWidget(self.word_edit_pushButton)

        self.word_delete_pushButton = QPushButton(self.tab)
        self.word_delete_pushButton.setObjectName(u"word_delete_pushButton")

        self.horizontalLayout.addWidget(self.word_delete_pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.word_tableView = QTableView(self.tab)
        self.word_tableView.setObjectName(u"word_tableView")

        self.verticalLayout_3.addWidget(self.word_tableView)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 994, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Word Group", None))
        self.word_group_new_pushButton.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.word_group_rename_pushButton.setText(QCoreApplication.translate("MainWindow", u"Rename", None))
        self.word_group_delete_pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.word_new_pushButton.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.word_edit_pushButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.word_delete_pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Words", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

