# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TestWordDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QRadioButton, QSizePolicy,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(552, 440)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMaximumSize(QSize(16777215, 120))
        self.textBrowser.setMouseTracking(False)
        self.textBrowser.setAcceptDrops(False)

        self.verticalLayout_2.addWidget(self.textBrowser)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton_1 = QRadioButton(Dialog)
        self.radioButton_1.setObjectName(u"radioButton_1")
        self.radioButton_1.setMaximumSize(QSize(600, 16777215))

        self.verticalLayout.addWidget(self.radioButton_1)

        self.radioButton_2 = QRadioButton(Dialog)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setMaximumSize(QSize(600, 16777215))

        self.verticalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(Dialog)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setMaximumSize(QSize(600, 16777215))

        self.verticalLayout.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(Dialog)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setMaximumSize(QSize(600, 16777215))

        self.verticalLayout.addWidget(self.radioButton_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Test Word", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt; font-weight:700;\">New Test!</span></p></body></html>", None))
        self.radioButton_1.setText(QCoreApplication.translate("Dialog", u"RadioButton", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"RadioButton", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"RadioButton", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"RadioButton", None))
    # retranslateUi

