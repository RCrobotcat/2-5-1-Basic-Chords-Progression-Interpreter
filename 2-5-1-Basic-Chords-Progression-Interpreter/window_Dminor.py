# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dminor.ui'
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QLabel, QListView,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextBrowser, QWidget)
import Dmin_rc

class Ui_DMin(object):
    def setupUi(self, DMin):
        if not DMin.objectName():
            DMin.setObjectName(u"DMin")
        DMin.resize(480, 378)
        DMin.setStyleSheet(u"background-color: rgb(197, 255, 170)")
        self.centralwidget = QWidget(DMin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.major_keys = QLabel(self.centralwidget)
        self.major_keys.setObjectName(u"major_keys")
        self.major_keys.setGeometry(QRect(10, 10, 381, 31))
        font = QFont()
        font.setFamilies([u"Baskerville Old Face"])
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        self.major_keys.setFont(font)
        self.showInMuseScore = QPushButton(self.centralwidget)
        self.showInMuseScore.setObjectName(u"showInMuseScore")
        self.showInMuseScore.setGeometry(QRect(10, 190, 281, 51))
        font1 = QFont()
        font1.setFamilies([u"Eras Bold ITC"])
        font1.setPointSize(15)
        self.showInMuseScore.setFont(font1)
        self.showInMuseScore.setStyleSheet(u"QPushButton\n"
"{\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color: rgb(255, 201, 6);   \n"
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
        self.BackButton = QPushButton(self.centralwidget)
        self.BackButton.setObjectName(u"BackButton")
        self.BackButton.setGeometry(QRect(10, 300, 75, 31))
        font2 = QFont()
        font2.setFamilies([u"Microsoft JhengHei"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.BackButton.setFont(font2)
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
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 250, 361, 31))
        font3 = QFont()
        font3.setFamilies([u"\u65b0\u5b8b\u4f53"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.label.setFont(font3)
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(130, 300, 341, 31))
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(10, 70, 461, 61))
        self.listView.setStyleSheet(u"border-image: url(:/Dminor.png);")
        self.generate_mid = QCommandLinkButton(self.centralwidget)
        self.generate_mid.setObjectName(u"generate_mid")
        self.generate_mid.setGeometry(QRect(210, 140, 181, 41))
        self.generate_mid.setStyleSheet(u"QCommandLinkButton\n"
"{\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color: rgb(211, 207, 255);   \n"
"    color:black;\n"
"      \n"
"}\n"
"QCommandLinkButton:pressed\n"
"{\n"
"    \n"
"    /*\u6309\u4e0b\u65f6\u5b57\u5411\u53f3\u79fb\u52a84\u50cf\u7d20*/  \n"
"    padding-left:4px;\n"
"    /*\u6309\u4e0b\u65f6\u5b57\u5411\u4e0b\u79fb\u52a84\u50cf\u7d20*/  \n"
"    padding-top:4px;\n"
"}")
        self.generate_xml = QCommandLinkButton(self.centralwidget)
        self.generate_xml.setObjectName(u"generate_xml")
        self.generate_xml.setGeometry(QRect(10, 140, 181, 41))
        self.generate_xml.setStyleSheet(u"QCommandLinkButton\n"
"{\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color: rgb(211, 207, 255);   \n"
"    color:black;\n"
"      \n"
"}\n"
"QCommandLinkButton:pressed\n"
"{\n"
"    \n"
"    /*\u6309\u4e0b\u65f6\u5b57\u5411\u53f3\u79fb\u52a84\u50cf\u7d20*/  \n"
"    padding-left:4px;\n"
"    /*\u6309\u4e0b\u65f6\u5b57\u5411\u4e0b\u79fb\u52a84\u50cf\u7d20*/  \n"
"    padding-top:4px;\n"
"}")
        self.major_keys_2 = QLabel(self.centralwidget)
        self.major_keys_2.setObjectName(u"major_keys_2")
        self.major_keys_2.setGeometry(QRect(10, 40, 381, 31))
        font4 = QFont()
        font4.setFamilies([u"Ink Free"])
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setUnderline(True)
        self.major_keys_2.setFont(font4)
        DMin.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(DMin)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 480, 22))
        DMin.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(DMin)
        self.statusbar.setObjectName(u"statusbar")
        DMin.setStatusBar(self.statusbar)

        self.retranslateUi(DMin)

        QMetaObject.connectSlotsByName(DMin)
    # setupUi

    def retranslateUi(self, DMin):
        DMin.setWindowTitle(QCoreApplication.translate("DMin", u"MainWindow", None))
        self.major_keys.setText(QCoreApplication.translate("DMin", u"2-5-1 Chord Progression in D Minor: ", None))
        self.showInMuseScore.setText(QCoreApplication.translate("DMin", u"Show this in MuseScore", None))
        self.BackButton.setText(QCoreApplication.translate("DMin", u" Go Back", None))
        self.label.setText(QCoreApplication.translate("DMin", u"\uff08If there's anything wrong, please email me.\n"
" \u5982\u679c\u6709\u9519\u8bef\uff0c\u8bf7\u90ae\u4ef6\u544a\u8bc9\u6211\u3002\uff09", None))
        self.textBrowser.setHtml(QCoreApplication.translate("DMin", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u4f5c\u8005\u90ae\u7bb1(Email): RCrobotcat@gmail.com</span></p></body></html>", None))
        self.generate_mid.setText(QCoreApplication.translate("DMin", u"Generate '.mid' file", None))
        self.generate_xml.setText(QCoreApplication.translate("DMin", u" Generate '.xml' file", None))
        self.major_keys_2.setText(QCoreApplication.translate("DMin", u"Em7b5 - A7 - Dm7", None))
    # retranslateUi

