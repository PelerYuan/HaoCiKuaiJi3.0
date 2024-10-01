# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QListView, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1229, 717)
        self.word_group_new_action = QAction(MainWindow)
        self.word_group_new_action.setObjectName(u"word_group_new_action")
        self.word_group_rename_action = QAction(MainWindow)
        self.word_group_rename_action.setObjectName(u"word_group_rename_action")
        self.word_group_delete_action = QAction(MainWindow)
        self.word_group_delete_action.setObjectName(u"word_group_delete_action")
        self.word_group_refresh_action = QAction(MainWindow)
        self.word_group_refresh_action.setObjectName(u"word_group_refresh_action")
        self.word_group_update_data_action = QAction(MainWindow)
        self.word_group_update_data_action.setObjectName(u"word_group_update_data_action")
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
        self.word_group_listView = QListView(self.groupBox)
        self.word_group_listView.setObjectName(u"word_group_listView")
        self.word_group_listView.setAcceptDrops(False)

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

        self.word_tableWidget = QTableWidget(self.tab)
        if (self.word_tableWidget.columnCount() < 5):
            self.word_tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.word_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.word_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.word_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.word_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.word_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.word_tableWidget.setObjectName(u"word_tableWidget")
        self.word_tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.word_tableWidget.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.word_tableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.word_tableWidget)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1229, 33))
        self.menuGroup = QMenu(self.menubar)
        self.menuGroup.setObjectName(u"menuGroup")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuGroup.menuAction())
        self.menuGroup.addAction(self.word_group_new_action)
        self.menuGroup.addSeparator()
        self.menuGroup.addAction(self.word_group_rename_action)
        self.menuGroup.addAction(self.word_group_delete_action)
        self.menuGroup.addSeparator()
        self.menuGroup.addAction(self.word_group_refresh_action)
        self.menuGroup.addAction(self.word_group_update_data_action)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"HaoCiKuaiJi3.0", None))
        self.word_group_new_action.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.word_group_rename_action.setText(QCoreApplication.translate("MainWindow", u"Rename", None))
        self.word_group_delete_action.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.word_group_refresh_action.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.word_group_update_data_action.setText(QCoreApplication.translate("MainWindow", u"Update Data", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Word Group ", None))
        self.word_new_pushButton.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.word_edit_pushButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.word_delete_pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        ___qtablewidgetitem = self.word_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Word", None));
        ___qtablewidgetitem1 = self.word_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Speech Of Part", None));
        ___qtablewidgetitem2 = self.word_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Definition", None));
        ___qtablewidgetitem3 = self.word_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Example", None));
        ___qtablewidgetitem4 = self.word_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Audio", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Words", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.menuGroup.setTitle(QCoreApplication.translate("MainWindow", u"Group", None))
    # retranslateUi

