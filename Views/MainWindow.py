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
from PySide6.QtWidgets import (QApplication, QComboBox, QCommandLinkButton, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QListView,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextBrowser, QToolBox,
    QVBoxLayout, QWidget)

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
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.toolBox = QToolBox(self.tab_2)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 1164, 561))
        self.verticalLayout_5 = QVBoxLayout(self.page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.textBrowser = QTextBrowser(self.page)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMouseTracking(False)
        self.textBrowser.setAcceptDrops(False)

        self.verticalLayout_5.addWidget(self.textBrowser)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.new_test_comboBox = QComboBox(self.page)
        self.new_test_comboBox.setObjectName(u"new_test_comboBox")

        self.horizontalLayout_2.addWidget(self.new_test_comboBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.new_test_commandLinkButton = QCommandLinkButton(self.page)
        self.new_test_commandLinkButton.setObjectName(u"new_test_commandLinkButton")

        self.horizontalLayout_3.addWidget(self.new_test_commandLinkButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"New Test")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 1164, 561))
        self.toolBox.addItem(self.page_2, u"Page 2")

        self.verticalLayout_4.addWidget(self.toolBox)

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

        self.tabWidget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(0)


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
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt; font-weight:700;\">New Test!</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"from group:", None))
        self.new_test_commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"GO", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"New Test", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Test", None))
        self.menuGroup.setTitle(QCoreApplication.translate("MainWindow", u"Group", None))
    # retranslateUi

