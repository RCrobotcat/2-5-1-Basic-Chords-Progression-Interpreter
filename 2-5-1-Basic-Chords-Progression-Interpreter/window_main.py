# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTextBrowser, QVBoxLayout, QWidget)

class Ui_Interpreter_main(object):
    def setupUi(self, Interpreter_main):
        if not Interpreter_main.objectName():
            Interpreter_main.setObjectName(u"Interpreter_main")
        Interpreter_main.resize(597, 423)
        Interpreter_main.setStyleSheet(u"background-color: rgb(170, 255, 255)")
        self.centralwidget = QWidget(Interpreter_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 0, 581, 261))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Rage Italic"])
        font.setPointSize(25)
        font.setItalic(False)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.title = QLabel(self.layoutWidget)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Bauhaus 93"])
        font1.setPointSize(24)
        font1.setWeight(QFont.Medium)
        font1.setItalic(False)
        font1.setUnderline(True)
        font1.setStrikeOut(False)
        self.title.setFont(font1)

        self.verticalLayout.addWidget(self.title)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.developer = QLabel(self.layoutWidget)
        self.developer.setObjectName(u"developer")
        font2 = QFont()
        font2.setFamilies([u"Cascadia Code"])
        font2.setPointSize(10)
        self.developer.setFont(font2)

        self.horizontalLayout.addWidget(self.developer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.startButton = QPushButton(self.layoutWidget)
        self.startButton.setObjectName(u"startButton")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(128, 255, 192, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.startButton.setPalette(palette)
        font3 = QFont()
        font3.setFamilies([u"Arial Black"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.startButton.setFont(font3)
        self.startButton.setStyleSheet(u"QPushButton\n"
"{\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color: rgb(128, 255, 192);\n"
"    /*\u5b57\u4f53\u989c\u8272\u4e3a\u767d\u8272*/    \n"
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

        self.verticalLayout.addWidget(self.startButton)

        self.quitButton = QPushButton(self.layoutWidget)
        self.quitButton.setObjectName(u"quitButton")
        self.quitButton.setFont(font3)
        self.quitButton.setStyleSheet(u"QPushButton\n"
"{\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color: rgb(128, 255, 192);\n"
"    /*\u5b57\u4f53\u989c\u8272\u4e3a\u767d\u8272*/    \n"
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

        self.verticalLayout.addWidget(self.quitButton)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 270, 341, 31))
        Interpreter_main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Interpreter_main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 597, 22))
        Interpreter_main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Interpreter_main)
        self.statusbar.setObjectName(u"statusbar")
        Interpreter_main.setStatusBar(self.statusbar)

        self.retranslateUi(Interpreter_main)

        QMetaObject.connectSlotsByName(Interpreter_main)
    # setupUi

    def retranslateUi(self, Interpreter_main):
        Interpreter_main.setWindowTitle(QCoreApplication.translate("Interpreter_main", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Interpreter_main", u"WELCOME TO:", None))
        self.title.setText(QCoreApplication.translate("Interpreter_main", u"2-5-1 Basic Chord Progression Interpreter", None))
        self.developer.setText(QCoreApplication.translate("Interpreter_main", u"By RCrobotcat", None))
        self.startButton.setText(QCoreApplication.translate("Interpreter_main", u"START", None))
        self.quitButton.setText(QCoreApplication.translate("Interpreter_main", u"QUIT", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Interpreter_main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u4f5c\u8005\u90ae\u7bb1(Email): RCrobotcat@gmail.com</span></p></body></html>", None))
    # retranslateUi

