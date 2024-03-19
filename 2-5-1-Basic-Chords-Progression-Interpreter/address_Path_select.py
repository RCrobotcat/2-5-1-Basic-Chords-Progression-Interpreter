# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'address_Path.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QPushButton,
    QSizePolicy, QToolButton, QWidget)

class Ui_addressPath(object):
    def setupUi(self, addressPath):
        if not addressPath.objectName():
            addressPath.setObjectName(u"addressPath")
        addressPath.resize(348, 107)
        addressPath.setStyleSheet(u"background-color: rgb(240, 240, 240)")
        self.comboBox = QComboBox(addressPath)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 50, 291, 21))
        self.comboBox.setStyleSheet(u"QComboBox\n"
"{\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color: rgb(255, 255, 255);\n"
"    color:black;\n"
"      \n"
"}")
        self.Browse = QToolButton(addressPath)
        self.Browse.setObjectName(u"Browse")
        self.Browse.setGeometry(QRect(310, 50, 31, 22))
        self.Browse.setStyleSheet(u"QToolButton\n"
"{\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color: rgb(255, 255, 255);   \n"
"    color:black;\n"
"      \n"
"}\n"
"QToolButton:pressed\n"
"{\n"
"    \n"
"    /*\u6309\u4e0b\u65f6\u5b57\u5411\u53f3\u79fb\u52a84\u50cf\u7d20*/  \n"
"    padding-left:4px;\n"
"    /*\u6309\u4e0b\u65f6\u5b57\u5411\u4e0b\u79fb\u52a84\u50cf\u7d20*/  \n"
"    padding-top:4px;\n"
"}")
        self.label = QLabel(addressPath)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 131, 31))
        font = QFont()
        font.setFamilies([u"Microsoft PhagsPa"])
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        self.label.setFont(font)
        self.Confirm = QPushButton(addressPath)
        self.Confirm.setObjectName(u"Confirm")
        self.Confirm.setGeometry(QRect(10, 80, 61, 21))
        font1 = QFont()
        font1.setFamilies([u"Microsoft PhagsPa"])
        font1.setPointSize(10)
        self.Confirm.setFont(font1)
        self.Confirm.setStyleSheet(u"QPushButton\n"
"{\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color: rgb(255, 255, 255);   \n"
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
        self.GoBack = QPushButton(addressPath)
        self.GoBack.setObjectName(u"GoBack")
        self.GoBack.setGeometry(QRect(260, 10, 75, 24))
        self.GoBack.setStyleSheet(u"QPushButton\n"
"{\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color: rgb(255, 255, 255);   \n"
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

        self.retranslateUi(addressPath)

        QMetaObject.connectSlotsByName(addressPath)
    # setupUi

    def retranslateUi(self, addressPath):
        addressPath.setWindowTitle(QCoreApplication.translate("addressPath", u"Form", None))
        self.Browse.setText(QCoreApplication.translate("addressPath", u"...", None))
        self.label.setText(QCoreApplication.translate("addressPath", u"Select Saving Path: \n"
" \u9009\u62e9\u4fdd\u5b58\u8def\u5f84\uff1a", None))
        self.Confirm.setText(QCoreApplication.translate("addressPath", u"Confirm", None))
        self.GoBack.setText(QCoreApplication.translate("addressPath", u"Go Back", None))
    # retranslateUi

