from PySide6.QtWidgets import QMainWindow, QFileDialog
from window_Dbmajor import Ui_DbMaj
from window_Dmajor import Ui_dMajor
from window_Ebmajor import Ui_Ebmaj
from window_Emajor import Ui_eMaj
from window_Fmajor import Ui_fMaj
from window_cmajor import Ui_cMajor
from window_F_major import Ui_F_major
from window_Gmajor import Ui_gMaj
from window_Abmajor import Ui_AbMaj
from window_Amajor import Ui_aMaj
from window_Bbmajor import Ui_BbMaj
from window_Bmajor import Ui_BMaj
from address_Path_select import Ui_addressPath
from Converter import xml_save, midi_save, GoMuseScore
from PySide6.QtCore import Signal
from musescore_address import Ui_museAdd


class SelectAddressWindow(QMainWindow):
    directorySelected = Signal(str)  # 添加信号，用于传递选定的目录

    def __init__(self, parent=None):
        super(SelectAddressWindow, self).__init__(parent)
        self.selected_directory = None
        self.ui = Ui_addressPath()
        self.ui.setupUi(self)
        self.bind()

    def bind(self):
        self.ui.Browse.clicked.connect(self.openDirectoryDialog)
        self.ui.Confirm.clicked.connect(self.onConfirm)
        self.ui.GoBack.clicked.connect(self.GoBack_handle)

    def openDirectoryDialog(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:  # 确保用户选择了一个目录
            index = self.ui.comboBox.findText(directory)  # 查找文本在comboBox中的索引
            print(index)
            if index == -1:  # 如果不存在
                self.ui.comboBox.addItem(directory)  # 添加新项
                self.ui.comboBox.setCurrentIndex(self.ui.comboBox.count() - 1)  # 设置为新添加项的索引
            else:
                self.ui.comboBox.setCurrentIndex(index)  # 设置为现有项的索引

    def onConfirm(self):
        self.selected_directory = self.ui.comboBox.currentText()  # 获取选定目录
        self.directorySelected.emit(self.selected_directory)  # 发出信号
        self.close()

    def GoBack_handle(self):
        self.hide()
        self.parent().show()  # 显示父窗口


class SelectAddressWindow_1(QMainWindow):
    directorySelected_1 = Signal(str)  # 添加信号，用于传递选定的目录

    def __init__(self, parent=None):
        super(SelectAddressWindow_1, self).__init__(parent)
        self.selected_directory = None
        self.ui = Ui_museAdd()
        self.ui.setupUi(self)
        self.bind()

    def bind(self):
        self.ui.Browse.clicked.connect(self.openDirectoryDialog)
        self.ui.Confirm.clicked.connect(self.onConfirm)
        self.ui.GoBack.clicked.connect(self.GoBack_handle)

    def openDirectoryDialog(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:  # 确保用户选择了一个目录
            index = self.ui.comboBox.findText(directory)  # 查找文本在comboBox中的索引
            print(index)
            if index == -1:  # 如果不存在
                self.ui.comboBox.addItem(directory)  # 添加新项
                self.ui.comboBox.setCurrentIndex(self.ui.comboBox.count() - 1)  # 设置为新添加项的索引
            else:
                self.ui.comboBox.setCurrentIndex(index)  # 设置为现有项的索引

    def onConfirm(self):
        self.selected_directory = self.ui.comboBox.currentText()  # 获取选定目录
        self.directorySelected_1.emit(self.selected_directory)  # 发出信号
        self.close()

    def GoBack_handle(self):
        self.hide()
        self.parent().show()  # 显示父窗口


class CMajorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(CMajorWindow, self).__init__(parent)
        self.directory_selected = None  # 用于存储选择的目录
        self.another_window = None
        self.xml_or_mid = None
        self.ui = Ui_cMajor()
        self.ui.setupUi(self)
        self.bind()

    def bind(self):
        self.ui.generate_xml.clicked.connect(self.Generate_xml_click)
        self.ui.generate_mid.clicked.connect(self.Generate_mid_click)
        self.ui.showInMuseScore.clicked.connect(self.GoMuseScore)
        self.ui.BackButton.clicked.connect(self.Go_back_handle_click)

    def Generate_mid_click(self):
        self.another_window = SelectAddressWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "mid"

    def Generate_xml_click(self):
        self.another_window = SelectAddressWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "xml"

    def GoMuseScore(self):
        self.another_window = SelectAddressWindow_1(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected_1.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "MuseScore"

    def on_directory_selected(self, directory):
        self.directory_selected = directory  # 存储用户选择的目录
        self.show()

        if self.xml_or_mid == "xml":
            xml_save(self.directory_selected, key="C major")  # 存为.xml文件
        elif self.xml_or_mid == "mid":
            midi_save(self.directory_selected, key="C major")  # 存为.mid文件
        elif self.xml_or_mid == "MuseScore":
            GoMuseScore(self.directory_selected, key="C major")  # 在MuseScore中打开乐谱

    def Go_back_handle_click(self):
        self.hide()
        if self.parent():
            self.parent().show()  # 显示父窗口


class DbMajorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(DbMajorWindow, self).__init__(parent)
        self.directory_selected = None  # 用于存储选择的目录
        self.another_window = None
        self.xml_or_mid = None
        self.ui = Ui_DbMaj()
        self.ui.setupUi(self)
        self.bind()

    def bind(self):
        self.ui.generate_xml.clicked.connect(self.Generate_xml_click)
        self.ui.generate_mid.clicked.connect(self.Generate_mid_click)
        self.ui.showInMuseScore.clicked.connect(self.GoMuseScore)
        self.ui.BackButton.clicked.connect(self.Go_back_handle_click)

    def Generate_mid_click(self):
        self.another_window = SelectAddressWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "mid"

    def Generate_xml_click(self):
        self.another_window = SelectAddressWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "xml"

    def GoMuseScore(self):
        self.another_window = SelectAddressWindow_1(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected_1.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "MuseScore"

    def on_directory_selected(self, directory):
        self.directory_selected = directory  # 存储用户选择的目录
        self.show()

        if self.xml_or_mid == "xml":
            xml_save(self.directory_selected, key="Db major")
        elif self.xml_or_mid == "mid":
            midi_save(self.directory_selected, key="Db major")
        elif self.xml_or_mid == "MuseScore":
            GoMuseScore(self.directory_selected, key="Db major")  # 在MuseScore中打开乐谱

    def Go_back_handle_click(self):
        self.hide()
        if self.parent():
            self.parent().show()  # 显示父窗口


class DMajorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(DMajorWindow, self).__init__(parent)
        self.directory_selected = None  # 用于存储选择的目录
        self.another_window = None
        self.xml_or_mid = None
        self.ui = Ui_dMajor()
        self.ui.setupUi(self)
        self.bind()

    def bind(self):
        self.ui.generate_xml.clicked.connect(self.Generate_xml_click)
        self.ui.generate_mid.clicked.connect(self.Generate_mid_click)
        self.ui.showInMuseScore.clicked.connect(self.GoMuseScore)
        self.ui.BackButton.clicked.connect(self.Go_back_handle_click)

    def Generate_mid_click(self):
        self.another_window = SelectAddressWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "mid"

    def Generate_xml_click(self):
        self.another_window = SelectAddressWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "xml"

    def GoMuseScore(self):
        self.another_window = SelectAddressWindow_1(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected_1.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "MuseScore"

    def on_directory_selected(self, directory):
        self.directory_selected = directory  # 存储用户选择的目录
        self.show()

        if self.xml_or_mid == "xml":
            xml_save(self.directory_selected, key="D major")
        elif self.xml_or_mid == "mid":
            midi_save(self.directory_selected, key="D major")
        elif self.xml_or_mid == "MuseScore":
            GoMuseScore(self.directory_selected, key="D major")  # 在MuseScore中打开乐谱

    def Go_back_handle_click(self):
        self.hide()
        if self.parent():
            self.parent().show()  # 显示父窗口


class EbMajorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(EbMajorWindow, self).__init__(parent)
        self.directory_selected = None  # 用于存储选择的目录
        self.another_window = None
        self.xml_or_mid = None
        self.ui = Ui_Ebmaj()
        self.ui.setupUi(self)
        self.bind()

    def bind(self):
        self.ui.generate_xml.clicked.connect(self.Generate_xml_click)
        self.ui.generate_mid.clicked.connect(self.Generate_mid_click)
        self.ui.showInMuseScore.clicked.connect(self.GoMuseScore)
        self.ui.BackButton.clicked.connect(self.Go_back_handle_click)

    def Generate_mid_click(self):
        self.another_window = SelectAddressWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "mid"

    def Generate_xml_click(self):
        self.another_window = SelectAddressWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "xml"

    def GoMuseScore(self):
        self.another_window = SelectAddressWindow_1(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected_1.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "MuseScore"

    def on_directory_selected(self, directory):
        self.directory_selected = directory  # 存储用户选择的目录
        self.show()

        if self.xml_or_mid == "xml":
            xml_save(self.directory_selected, key="Eb major")
        elif self.xml_or_mid == "mid":
            midi_save(self.directory_selected, key="Eb major")
        elif self.xml_or_mid == "MuseScore":
            GoMuseScore(self.directory_selected, key="Eb major")  # 在MuseScore中打开乐谱

    def Go_back_handle_click(self):
        self.hide()
        if self.parent():
            self.parent().show()  # 显示父窗口


class EMajorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(EMajorWindow, self).__init__(parent)
        self.directory_selected = None  # 用于存储选择的目录
        self.another_window = None
        self.xml_or_mid = None
        self.ui = Ui_eMaj()
        self.ui.setupUi(self)
        self.bind()

    def bind(self):
        self.ui.generate_xml.clicked.connect(self.Generate_xml_click)
        self.ui.generate_mid.clicked.connect(self.Generate_mid_click)
        self.ui.showInMuseScore.clicked.connect(self.GoMuseScore)
        self.ui.BackButton.clicked.connect(self.Go_back_handle_click)

    def Generate_mid_click(self):
        self.another_window = SelectAddressWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "mid"

    def Generate_xml_click(self):
        self.another_window = SelectAddressWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "xml"

    def GoMuseScore(self):
        self.another_window = SelectAddressWindow_1(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected_1.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "MuseScore"

    def on_directory_selected(self, directory):
        self.directory_selected = directory  # 存储用户选择的目录
        self.show()

        if self.xml_or_mid == "xml":
            xml_save(self.directory_selected, key="E major")
        elif self.xml_or_mid == "mid":
            midi_save(self.directory_selected, key="E major")
        elif self.xml_or_mid == "MuseScore":
            GoMuseScore(self.directory_selected, key="E major")  # 在MuseScore中打开乐谱

    def Go_back_handle_click(self):
        self.hide()
        if self.parent():
            self.parent().show()  # 显示父窗口


class FMajorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(FMajorWindow, self).__init__(parent)
        self.directory_selected = None  # 用于存储选择的目录
        self.another_window = None
        self.xml_or_mid = None
        self.ui = Ui_fMaj()
        self.ui.setupUi(self)
        self.bind()

    def bind(self):
        self.ui.generate_xml.clicked.connect(self.Generate_xml_click)
        self.ui.generate_mid.clicked.connect(self.Generate_mid_click)
        self.ui.showInMuseScore.clicked.connect(self.GoMuseScore)
        self.ui.BackButton.clicked.connect(self.Go_back_handle_click)

    def Generate_mid_click(self):
        self.another_window = SelectAddressWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "mid"

    def Generate_xml_click(self):
        self.another_window = SelectAddressWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "xml"

    def GoMuseScore(self):
        self.another_window = SelectAddressWindow_1(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected_1.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "MuseScore"

    def on_directory_selected(self, directory):
        self.directory_selected = directory  # 存储用户选择的目录
        self.show()

        if self.xml_or_mid == "xml":
            xml_save(self.directory_selected, key="F major")
        elif self.xml_or_mid == "mid":
            midi_save(self.directory_selected, key="F major")
        elif self.xml_or_mid == "MuseScore":
            GoMuseScore(self.directory_selected, key="F major")  # 在MuseScore中打开乐谱

    def Go_back_handle_click(self):
        self.hide()
        if self.parent():
            self.parent().show()  # 显示父窗口


class F_MajorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(F_MajorWindow, self).__init__(parent)
        self.directory_selected = None  # 用于存储选择的目录
        self.another_window = None
        self.xml_or_mid = None
        self.ui = Ui_F_major()
        self.ui.setupUi(self)
        self.bind()

    def bind(self):
        self.ui.generate_xml.clicked.connect(self.Generate_xml_click)
        self.ui.generate_mid.clicked.connect(self.Generate_mid_click)
        self.ui.showInMuseScore.clicked.connect(self.GoMuseScore)
        self.ui.BackButton.clicked.connect(self.Go_back_handle_click)

    def Generate_mid_click(self):
        self.another_window = SelectAddressWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "mid"

    def Generate_xml_click(self):
        self.another_window = SelectAddressWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "xml"

    def GoMuseScore(self):
        self.another_window = SelectAddressWindow_1(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected_1.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "MuseScore"

    def on_directory_selected(self, directory):
        self.directory_selected = directory  # 存储用户选择的目录
        self.show()

        if self.xml_or_mid == "xml":
            xml_save(self.directory_selected, key="F# major")
        elif self.xml_or_mid == "mid":
            midi_save(self.directory_selected, key="F# major")
        elif self.xml_or_mid == "MuseScore":
            GoMuseScore(self.directory_selected, key="F# major")  # 在MuseScore中打开乐谱

    def Go_back_handle_click(self):
        self.hide()
        if self.parent():
            self.parent().show()  # 显示父窗口


class GMajorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(GMajorWindow, self).__init__(parent)
        self.directory_selected = None  # 用于存储选择的目录
        self.another_window = None
        self.xml_or_mid = None
        self.ui = Ui_gMaj()
        self.ui.setupUi(self)
        self.bind()

    def bind(self):
        self.ui.generate_xml.clicked.connect(self.Generate_xml_click)
        self.ui.generate_mid.clicked.connect(self.Generate_mid_click)
        self.ui.showInMuseScore.clicked.connect(self.GoMuseScore)
        self.ui.BackButton.clicked.connect(self.Go_back_handle_click)

    def Generate_mid_click(self):
        self.another_window = SelectAddressWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "mid"

    def Generate_xml_click(self):
        self.another_window = SelectAddressWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "xml"

    def GoMuseScore(self):
        self.another_window = SelectAddressWindow_1(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected_1.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "MuseScore"

    def on_directory_selected(self, directory):
        self.directory_selected = directory  # 存储用户选择的目录
        self.show()

        if self.xml_or_mid == "xml":
            xml_save(self.directory_selected, key="G major")
        elif self.xml_or_mid == "mid":
            midi_save(self.directory_selected, key="G major")
        elif self.xml_or_mid == "MuseScore":
            GoMuseScore(self.directory_selected, key="G major")  # 在MuseScore中打开乐谱

    def Go_back_handle_click(self):
        self.hide()
        if self.parent():
            self.parent().show()  # 显示父窗口


class AbMajorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AbMajorWindow, self).__init__(parent)
        self.directory_selected = None  # 用于存储选择的目录
        self.another_window = None
        self.xml_or_mid = None
        self.ui = Ui_AbMaj()
        self.ui.setupUi(self)
        self.bind()

    def bind(self):
        self.ui.generate_xml.clicked.connect(self.Generate_xml_click)
        self.ui.generate_mid.clicked.connect(self.Generate_mid_click)
        self.ui.showInMuseScore.clicked.connect(self.GoMuseScore)
        self.ui.BackButton.clicked.connect(self.Go_back_handle_click)

    def Generate_mid_click(self):
        self.another_window = SelectAddressWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "mid"

    def Generate_xml_click(self):
        self.another_window = SelectAddressWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "xml"

    def GoMuseScore(self):
        self.another_window = SelectAddressWindow_1(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected_1.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "MuseScore"

    def on_directory_selected(self, directory):
        self.directory_selected = directory  # 存储用户选择的目录
        self.show()

        if self.xml_or_mid == "xml":
            xml_save(self.directory_selected, key="Ab major")
        elif self.xml_or_mid == "mid":
            midi_save(self.directory_selected, key="Ab major")
        elif self.xml_or_mid == "MuseScore":
            GoMuseScore(self.directory_selected, key="Ab major")  # 在MuseScore中打开乐谱

    def Go_back_handle_click(self):
        self.hide()
        if self.parent():
            self.parent().show()  # 显示父窗口


class AMajorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AMajorWindow, self).__init__(parent)
        self.directory_selected = None  # 用于存储选择的目录
        self.another_window = None
        self.xml_or_mid = None
        self.ui = Ui_aMaj()
        self.ui.setupUi(self)
        self.bind()

    def bind(self):
        self.ui.generate_xml.clicked.connect(self.Generate_xml_click)
        self.ui.generate_mid.clicked.connect(self.Generate_mid_click)
        self.ui.showInMuseScore.clicked.connect(self.GoMuseScore)
        self.ui.BackButton.clicked.connect(self.Go_back_handle_click)

    def Generate_mid_click(self):
        self.another_window = SelectAddressWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "mid"

    def Generate_xml_click(self):
        self.another_window = SelectAddressWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "xml"

    def GoMuseScore(self):
        self.another_window = SelectAddressWindow_1(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected_1.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "MuseScore"

    def on_directory_selected(self, directory):
        self.directory_selected = directory  # 存储用户选择的目录
        self.show()

        if self.xml_or_mid == "xml":
            xml_save(self.directory_selected, key="A major")
        elif self.xml_or_mid == "mid":
            midi_save(self.directory_selected, key="A major")
        elif self.xml_or_mid == "MuseScore":
            GoMuseScore(self.directory_selected, key="A major")  # 在MuseScore中打开乐谱

    def Go_back_handle_click(self):
        self.hide()
        if self.parent():
            self.parent().show()  # 显示父窗口


class BbMajorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(BbMajorWindow, self).__init__(parent)
        self.directory_selected = None  # 用于存储选择的目录
        self.another_window = None
        self.xml_or_mid = None
        self.ui = Ui_BbMaj()
        self.ui.setupUi(self)
        self.bind()

    def bind(self):
        self.ui.generate_xml.clicked.connect(self.Generate_xml_click)
        self.ui.generate_mid.clicked.connect(self.Generate_mid_click)
        self.ui.showInMuseScore.clicked.connect(self.GoMuseScore)
        self.ui.BackButton.clicked.connect(self.Go_back_handle_click)

    def Generate_mid_click(self):
        self.another_window = SelectAddressWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "mid"

    def Generate_xml_click(self):
        self.another_window = SelectAddressWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "xml"

    def GoMuseScore(self):
        self.another_window = SelectAddressWindow_1(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected_1.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "MuseScore"

    def on_directory_selected(self, directory):
        self.directory_selected = directory  # 存储用户选择的目录
        self.show()

        if self.xml_or_mid == "xml":
            xml_save(self.directory_selected, key="Bb major")
        elif self.xml_or_mid == "mid":
            midi_save(self.directory_selected, key="Bb major")
        elif self.xml_or_mid == "MuseScore":
            GoMuseScore(self.directory_selected, key="Bb major")  # 在MuseScore中打开乐谱

    def Go_back_handle_click(self):
        self.hide()
        if self.parent():
            self.parent().show()  # 显示父窗口


class BMajorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(BMajorWindow, self).__init__(parent)
        self.directory_selected = None  # 用于存储选择的目录
        self.another_window = None
        self.xml_or_mid = None
        self.ui = Ui_BMaj()
        self.ui.setupUi(self)
        self.bind()

    def bind(self):
        self.ui.generate_xml.clicked.connect(self.Generate_xml_click)
        self.ui.generate_mid.clicked.connect(self.Generate_mid_click)
        self.ui.showInMuseScore.clicked.connect(self.GoMuseScore)
        self.ui.BackButton.clicked.connect(self.Go_back_handle_click)

    def Generate_mid_click(self):
        self.another_window = SelectAddressWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "mid"

    def Generate_xml_click(self):
        self.another_window = SelectAddressWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "xml"

    def GoMuseScore(self):
        self.another_window = SelectAddressWindow_1(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

        self.another_window.directorySelected_1.connect(self.on_directory_selected)  # 接收信号
        self.xml_or_mid = "MuseScore"

    def on_directory_selected(self, directory):
        self.directory_selected = directory  # 存储用户选择的目录
        self.show()

        if self.xml_or_mid == "xml":
            xml_save(self.directory_selected, key="B major")
        elif self.xml_or_mid == "mid":
            midi_save(self.directory_selected, key="B major")
        elif self.xml_or_mid == "MuseScore":
            GoMuseScore(self.directory_selected, key="B major")  # 在MuseScore中打开乐谱

    def Go_back_handle_click(self):
        self.hide()
        if self.parent():
            self.parent().show()  # 显示父窗口
