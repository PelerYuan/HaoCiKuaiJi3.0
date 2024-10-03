# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MemorizeWordDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QPushButton,
    QSizePolicy, QTextBrowser, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(552, 440)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.word_textBrowser = QTextBrowser(Dialog)
        self.word_textBrowser.setObjectName(u"word_textBrowser")
        self.word_textBrowser.setMaximumSize(QSize(16777215, 120))
        self.word_textBrowser.setMouseTracking(False)
        self.word_textBrowser.setAcceptDrops(False)

        self.verticalLayout.addWidget(self.word_textBrowser)

        self.example_textBrowser = QTextBrowser(Dialog)
        self.example_textBrowser.setObjectName(u"example_textBrowser")

        self.verticalLayout.addWidget(self.example_textBrowser)

        self.yes_pushButton = QPushButton(Dialog)
        self.yes_pushButton.setObjectName(u"yes_pushButton")

        self.verticalLayout.addWidget(self.yes_pushButton)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.no_pushButton = QPushButton(Dialog)
        self.no_pushButton.setObjectName(u"no_pushButton")

        self.horizontalLayout.addWidget(self.no_pushButton)

        self.tip_pushButton = QPushButton(Dialog)
        self.tip_pushButton.setObjectName(u"tip_pushButton")

        self.horizontalLayout.addWidget(self.tip_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Memorize Word", None))
        self.word_textBrowser.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt; font-weight:700;\">New Memorize!</span></p></body></html>", None))
        self.yes_pushButton.setText(QCoreApplication.translate("Dialog", u"I know", None))
        self.no_pushButton.setText(QCoreApplication.translate("Dialog", u"I don't know", None))
        self.tip_pushButton.setText(QCoreApplication.translate("Dialog", u"Give me the tip", None))
    # retranslateUi

