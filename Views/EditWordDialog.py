# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditWordDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGroupBox, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(679, 596)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.word_lineEdit = QLineEdit(self.groupBox)
        self.word_lineEdit.setObjectName(u"word_lineEdit")
        self.word_lineEdit.setReadOnly(False)

        self.horizontalLayout.addWidget(self.word_lineEdit)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.part_lineEdit = QLineEdit(self.groupBox_2)
        self.part_lineEdit.setObjectName(u"part_lineEdit")

        self.horizontalLayout_2.addWidget(self.part_lineEdit)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.symbol_lineEdit = QLineEdit(self.groupBox_3)
        self.symbol_lineEdit.setObjectName(u"symbol_lineEdit")

        self.horizontalLayout_3.addWidget(self.symbol_lineEdit)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.meaning_textEdit = QTextEdit(self.tab_2)
        self.meaning_textEdit.setObjectName(u"meaning_textEdit")

        self.verticalLayout_3.addWidget(self.meaning_textEdit)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_4 = QVBoxLayout(self.tab_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.example_textEdit = QTextEdit(self.tab_4)
        self.example_textEdit.setObjectName(u"example_textEdit")

        self.verticalLayout_4.addWidget(self.example_textEdit)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_5 = QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_4 = QGroupBox(self.tab_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.audio_lineEdit = QLineEdit(self.groupBox_4)
        self.audio_lineEdit.setObjectName(u"audio_lineEdit")

        self.horizontalLayout_4.addWidget(self.audio_lineEdit)


        self.verticalLayout_5.addWidget(self.groupBox_4)

        self.audio_test_pushButton = QPushButton(self.tab_3)
        self.audio_test_pushButton.setObjectName(u"audio_test_pushButton")

        self.verticalLayout_5.addWidget(self.audio_test_pushButton)

        self.verticalSpacer_2 = QSpacerItem(20, 384, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"EditWord", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Word", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Part", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Symbol", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Basic Information", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Meaning", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Dialog", u"Example", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"URL", None))
        self.audio_test_pushButton.setText(QCoreApplication.translate("Dialog", u"Test", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Dialog", u"Audio", None))
    # retranslateUi

