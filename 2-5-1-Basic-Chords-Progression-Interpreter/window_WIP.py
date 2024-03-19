# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WIP.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_wip(object):
    def setupUi(self, wip):
        if not wip.objectName():
            wip.setObjectName(u"wip")
        wip.resize(279, 69)
        self.label = QLabel(wip)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 231, 31))
        font = QFont()
        font.setFamilies([u"Lucida Sans Unicode"])
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.BackButton = QPushButton(wip)
        self.BackButton.setObjectName(u"BackButton")
        self.BackButton.setGeometry(QRect(230, 40, 41, 21))
        self.BackButton.setStyleSheet(u"QPushButton\n"
"{\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color: rgb(170, 255, 255);   \n"
"    color:black;\n"
"      \n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    \n"
"    /*\u6309\u4e0b\u65f6\u5b57\u5411\u53f3\u79fb\u52a84\u50cf\u7d20*/  \n"
"    padding-left:4px;\n"
"    /*\u6309\u4e0b\u65f6\u5b57\u5411\u4e0b\u79fb\u52a84\u50cf\u7d20*/  \n"
"    padding-top:4px;\n"
"}")

        self.retranslateUi(wip)

        QMetaObject.connectSlotsByName(wip)
    # setupUi

    def retranslateUi(self, wip):
        wip.setWindowTitle(QCoreApplication.translate("wip", u"Form", None))
        self.label.setText(QCoreApplication.translate("wip", u"Work In Progress !", None))
        self.BackButton.setText(QCoreApplication.translate("wip", u" Back", None))
    # retranslateUi

