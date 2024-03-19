# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setKeys.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QListView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QToolButton,
    QWidget)
import image_1_rc

class Ui_setKeys(object):
    def setupUi(self, setKeys):
        if not setKeys.objectName():
            setKeys.setObjectName(u"setKeys")
        setKeys.resize(504, 384)
        setKeys.setStyleSheet(u"background-color: rgb(211, 255, 153)")
        self.centralwidget = QWidget(setKeys)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Fmaj = QPushButton(self.centralwidget)
        self.Fmaj.setObjectName(u"Fmaj")
        self.Fmaj.setGeometry(QRect(20, 90, 75, 24))
        self.Fmaj.setStyleSheet(u"QPushButton\n"
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
        self.Emaj = QPushButton(self.centralwidget)
        self.Emaj.setObjectName(u"Emaj")
        self.Emaj.setGeometry(QRect(400, 60, 75, 24))
        self.Emaj.setStyleSheet(u"QPushButton\n"
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
        self.Gmaj = QPushButton(self.centralwidget)
        self.Gmaj.setObjectName(u"Gmaj")
        self.Gmaj.setGeometry(QRect(210, 90, 75, 24))
        self.Gmaj.setStyleSheet(u"QPushButton\n"
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
        self.Amaj = QPushButton(self.centralwidget)
        self.Amaj.setObjectName(u"Amaj")
        self.Amaj.setGeometry(QRect(400, 90, 75, 24))
        self.Amaj.setStyleSheet(u"QPushButton\n"
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
        self.minor_keys = QLabel(self.centralwidget)
        self.minor_keys.setObjectName(u"minor_keys")
        self.minor_keys.setGeometry(QRect(20, 160, 191, 31))
        font = QFont()
        font.setFamilies([u"Baskerville Old Face"])
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        self.minor_keys.setFont(font)
        self.Ebmaj = QPushButton(self.centralwidget)
        self.Ebmaj.setObjectName(u"Ebmaj")
        self.Ebmaj.setGeometry(QRect(300, 60, 75, 24))
        self.Ebmaj.setStyleSheet(u"QPushButton\n"
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
        self.Dm = QPushButton(self.centralwidget)
        self.Dm.setObjectName(u"Dm")
        self.Dm.setGeometry(QRect(210, 200, 75, 24))
        self.Dm.setStyleSheet(u"QPushButton\n"
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
        self.Dmaj = QPushButton(self.centralwidget)
        self.Dmaj.setObjectName(u"Dmaj")
        self.Dmaj.setGeometry(QRect(210, 60, 75, 24))
        self.Dmaj.setStyleSheet(u"QPushButton\n"
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
        self.Ebm = QPushButton(self.centralwidget)
        self.Ebm.setObjectName(u"Ebm")
        self.Ebm.setGeometry(QRect(300, 200, 75, 24))
        self.Ebm.setStyleSheet(u"QPushButton\n"
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
        self.Dbmaj = QPushButton(self.centralwidget)
        self.Dbmaj.setObjectName(u"Dbmaj")
        self.Dbmaj.setGeometry(QRect(120, 60, 75, 24))
        self.Dbmaj.setStyleSheet(u"QPushButton\n"
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
        self.Cmaj = QPushButton(self.centralwidget)
        self.Cmaj.setObjectName(u"Cmaj")
        self.Cmaj.setGeometry(QRect(20, 60, 75, 24))
        self.Cmaj.setStyleSheet(u"QPushButton\n"
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
        self.Em = QPushButton(self.centralwidget)
        self.Em.setObjectName(u"Em")
        self.Em.setGeometry(QRect(400, 200, 75, 24))
        self.Em.setStyleSheet(u"QPushButton\n"
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
        self.Gm = QPushButton(self.centralwidget)
        self.Gm.setObjectName(u"Gm")
        self.Gm.setGeometry(QRect(210, 230, 75, 24))
        self.Gm.setStyleSheet(u"QPushButton\n"
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
        self.Abmaj = QPushButton(self.centralwidget)
        self.Abmaj.setObjectName(u"Abmaj")
        self.Abmaj.setGeometry(QRect(300, 90, 75, 24))
        self.Abmaj.setStyleSheet(u"QPushButton\n"
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
        self.major_keys = QLabel(self.centralwidget)
        self.major_keys.setObjectName(u"major_keys")
        self.major_keys.setGeometry(QRect(20, 10, 201, 31))
        self.major_keys.setFont(font)
        self.Cm = QPushButton(self.centralwidget)
        self.Cm.setObjectName(u"Cm")
        self.Cm.setGeometry(QRect(20, 200, 75, 24))
        self.Cm.setStyleSheet(u"QPushButton\n"
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
        self.F_sharp_maj = QPushButton(self.centralwidget)
        self.F_sharp_maj.setObjectName(u"F_sharp_maj")
        self.F_sharp_maj.setGeometry(QRect(120, 90, 75, 24))
        self.F_sharp_maj.setStyleSheet(u"QPushButton\n"
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
        self.Bmaj = QPushButton(self.centralwidget)
        self.Bmaj.setObjectName(u"Bmaj")
        self.Bmaj.setGeometry(QRect(120, 120, 75, 24))
        self.Bmaj.setStyleSheet(u"QPushButton\n"
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
        self.Am = QPushButton(self.centralwidget)
        self.Am.setObjectName(u"Am")
        self.Am.setGeometry(QRect(400, 230, 75, 24))
        self.Am.setStyleSheet(u"QPushButton\n"
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
        self.Bm = QPushButton(self.centralwidget)
        self.Bm.setObjectName(u"Bm")
        self.Bm.setGeometry(QRect(120, 260, 75, 24))
        self.Bm.setStyleSheet(u"QPushButton\n"
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
        self.Bbmaj = QPushButton(self.centralwidget)
        self.Bbmaj.setObjectName(u"Bbmaj")
        self.Bbmaj.setGeometry(QRect(20, 120, 75, 24))
        self.Bbmaj.setStyleSheet(u"QPushButton\n"
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
        self.Dbm = QPushButton(self.centralwidget)
        self.Dbm.setObjectName(u"Dbm")
        self.Dbm.setGeometry(QRect(120, 200, 75, 24))
        self.Dbm.setStyleSheet(u"QPushButton\n"
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
        self.Bbm = QPushButton(self.centralwidget)
        self.Bbm.setObjectName(u"Bbm")
        self.Bbm.setGeometry(QRect(20, 260, 75, 24))
        self.Bbm.setStyleSheet(u"QPushButton\n"
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
        self.F_sharp_m = QPushButton(self.centralwidget)
        self.F_sharp_m.setObjectName(u"F_sharp_m")
        self.F_sharp_m.setGeometry(QRect(120, 230, 75, 24))
        self.F_sharp_m.setStyleSheet(u"QPushButton\n"
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
        self.Fm = QPushButton(self.centralwidget)
        self.Fm.setObjectName(u"Fm")
        self.Fm.setGeometry(QRect(20, 230, 75, 24))
        self.Fm.setStyleSheet(u"QPushButton\n"
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
        self.Abm = QPushButton(self.centralwidget)
        self.Abm.setObjectName(u"Abm")
        self.Abm.setGeometry(QRect(300, 230, 75, 24))
        self.Abm.setStyleSheet(u"QPushButton\n"
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
        self.minor_keys_2 = QLabel(self.centralwidget)
        self.minor_keys_2.setObjectName(u"minor_keys_2")
        self.minor_keys_2.setGeometry(QRect(20, 300, 81, 31))
        self.minor_keys_2.setFont(font)
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(20, 330, 31, 31))
        self.toolButton.setStyleSheet(u"QToolButton\n"
"{\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color: rgb(170, 255, 255);   \n"
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
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(230, -10, 281, 421))
        self.listView.setStyleSheet(u"border-image: url(:/300.jpg);")
        self.BackButton = QPushButton(self.centralwidget)
        self.BackButton.setObjectName(u"BackButton")
        self.BackButton.setGeometry(QRect(70, 330, 75, 31))
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
        setKeys.setCentralWidget(self.centralwidget)
        self.listView.raise_()
        self.Fmaj.raise_()
        self.Emaj.raise_()
        self.Gmaj.raise_()
        self.Amaj.raise_()
        self.minor_keys.raise_()
        self.Ebmaj.raise_()
        self.Dm.raise_()
        self.Dmaj.raise_()
        self.Ebm.raise_()
        self.Dbmaj.raise_()
        self.Cmaj.raise_()
        self.Em.raise_()
        self.Gm.raise_()
        self.Abmaj.raise_()
        self.major_keys.raise_()
        self.Cm.raise_()
        self.F_sharp_maj.raise_()
        self.Bmaj.raise_()
        self.Am.raise_()
        self.Bm.raise_()
        self.Bbmaj.raise_()
        self.Dbm.raise_()
        self.Bbm.raise_()
        self.F_sharp_m.raise_()
        self.Fm.raise_()
        self.Abm.raise_()
        self.minor_keys_2.raise_()
        self.toolButton.raise_()
        self.BackButton.raise_()
        self.menubar = QMenuBar(setKeys)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 504, 22))
        setKeys.setMenuBar(self.menubar)

        self.retranslateUi(setKeys)

        QMetaObject.connectSlotsByName(setKeys)
    # setupUi

    def retranslateUi(self, setKeys):
        setKeys.setWindowTitle(QCoreApplication.translate("setKeys", u"MainWindow", None))
        self.Fmaj.setText(QCoreApplication.translate("setKeys", u"F", None))
        self.Emaj.setText(QCoreApplication.translate("setKeys", u"E", None))
        self.Gmaj.setText(QCoreApplication.translate("setKeys", u"G", None))
        self.Amaj.setText(QCoreApplication.translate("setKeys", u"A", None))
        self.minor_keys.setText(QCoreApplication.translate("setKeys", u"Minor Keys' 2-5-1: ", None))
        self.Ebmaj.setText(QCoreApplication.translate("setKeys", u"Eb", None))
        self.Dm.setText(QCoreApplication.translate("setKeys", u"D", None))
        self.Dmaj.setText(QCoreApplication.translate("setKeys", u"D", None))
        self.Ebm.setText(QCoreApplication.translate("setKeys", u"Eb", None))
        self.Dbmaj.setText(QCoreApplication.translate("setKeys", u"Db", None))
        self.Cmaj.setText(QCoreApplication.translate("setKeys", u"C", None))
        self.Em.setText(QCoreApplication.translate("setKeys", u"E", None))
        self.Gm.setText(QCoreApplication.translate("setKeys", u"G", None))
        self.Abmaj.setText(QCoreApplication.translate("setKeys", u"Ab", None))
        self.major_keys.setText(QCoreApplication.translate("setKeys", u"Major Keys' 2-5-1: ", None))
        self.Cm.setText(QCoreApplication.translate("setKeys", u"C", None))
        self.F_sharp_maj.setText(QCoreApplication.translate("setKeys", u"F#", None))
        self.Bmaj.setText(QCoreApplication.translate("setKeys", u"B", None))
        self.Am.setText(QCoreApplication.translate("setKeys", u"A", None))
        self.Bm.setText(QCoreApplication.translate("setKeys", u"B", None))
        self.Bbmaj.setText(QCoreApplication.translate("setKeys", u"Bb", None))
        self.Dbm.setText(QCoreApplication.translate("setKeys", u"Db", None))
        self.Bbm.setText(QCoreApplication.translate("setKeys", u"Bb", None))
        self.F_sharp_m.setText(QCoreApplication.translate("setKeys", u"F#", None))
        self.Fm.setText(QCoreApplication.translate("setKeys", u"F", None))
        self.Abm.setText(QCoreApplication.translate("setKeys", u"Ab", None))
        self.minor_keys_2.setText(QCoreApplication.translate("setKeys", u"Others: ", None))
        self.toolButton.setText(QCoreApplication.translate("setKeys", u"...", None))
        self.BackButton.setText(QCoreApplication.translate("setKeys", u" Go Back", None))
    # retranslateUi

