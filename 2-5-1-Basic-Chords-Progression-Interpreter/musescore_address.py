# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'musescore_address.ui'
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

class Ui_museAdd(object):
    def setupUi(self, museAdd):
        if not museAdd.objectName():
            museAdd.setObjectName(u"museAdd")
        museAdd.resize(347, 108)
        self.Confirm = QPushButton(museAdd)
        self.Confirm.setObjectName(u"Confirm")
        self.Confirm.setGeometry(QRect(10, 80, 61, 21))
        font = QFont()
        font.setFamilies([u"Microsoft PhagsPa"])
        font.setPointSize(10)
        self.Confirm.setFont(font)
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
        self.Browse = QToolButton(museAdd)
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
        self.comboBox = QComboBox(museAdd)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 50, 291, 21))
        self.comboBox.setStyleSheet(u"QComboBox\n"
"{\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color: rgb(255, 255, 255);\n"
"    color:black;\n"
"      \n"
"}")
        self.GoBack = QPushButton(museAdd)
        self.GoBack.setObjectName(u"GoBack")
        self.GoBack.setGeometry(QRect(270, 80, 71, 21))
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
        self.label = QLabel(museAdd)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 281, 31))
        font1 = QFont()
        font1.setFamilies([u"Microsoft PhagsPa"])
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setUnderline(False)
        self.label.setFont(font1)

        self.retranslateUi(museAdd)

        QMetaObject.connectSlotsByName(museAdd)
    # setupUi

    def retranslateUi(self, museAdd):
        museAdd.setWindowTitle(QCoreApplication.translate("museAdd", u"Form", None))
        self.Confirm.setText(QCoreApplication.translate("museAdd", u"Confirm", None))
        self.Browse.setText(QCoreApplication.translate("museAdd", u"...", None))
        self.GoBack.setText(QCoreApplication.translate("museAdd", u"Go Back", None))
        self.label.setText(QCoreApplication.translate("museAdd", u"Select the folder path where MuseScore4.exe is located: \n"
" \u9009\u62e9MuseScore4.exe\u6240\u5728\u7684\u6587\u4ef6\u5939\u8def\u5f84\uff1a", None))
    # retranslateUi

