from address_Path_select import Ui_addressPath
from Converter import xml_save, midi_save, GoMuseScore
from PySide6.QtCore import Signal
from musescore_address import Ui_museAdd
from PySide6.QtWidgets import QMainWindow, QFileDialog
from window_Cminor import Ui_cMin
from window_Dbminor import Ui_DbMin
from window_Eminor import Ui_EMin
from window_Dminor import Ui_DMin
from window_Ebminor import Ui_EbMin
from window_Fminor import Ui_FMin
from window_F_minor import Ui_F_min
from window_Gminor import Ui_GMin
from window_Abminor import Ui_AbMin
from window_Aminor import Ui_AMin
from window_Bbminor import Ui_BbMin
from window_Bminor import Ui_BMin


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


class CMinorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(CMinorWindow, self).__init__(parent)
        self.directory_selected = None  # 用于存储选择的目录
        self.another_window = None
        self.xml_or_mid = None
        self.ui = Ui_cMin()
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
            xml_save(self.directory_selected, key="C minor")  # 存为.xml文件
        elif self.xml_or_mid == "mid":
            midi_save(self.directory_selected, key="C minor")  # 存为.mid文件
        elif self.xml_or_mid == "MuseScore":
            GoMuseScore(self.directory_selected, key="C minor")  # 在MuseScore中打开乐谱

    def Go_back_handle_click(self):
        self.hide()
        if self.parent():
            self.parent().show()  # 显示父窗口


class DbMinorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(DbMinorWindow, self).__init__(parent)
        self.directory_selected = None  # 用于存储选择的目录
        self.another_window = None
        self.xml_or_mid = None
        self.ui = Ui_DbMin()
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
            xml_save(self.directory_selected, key="Db minor")  # 存为.xml文件
        elif self.xml_or_mid == "mid":
            midi_save(self.directory_selected, key="Db minor")  # 存为.mid文件
        elif self.xml_or_mid == "MuseScore":
            GoMuseScore(self.directory_selected, key="Db minor")  # 在MuseScore中打开乐谱

    def Go_back_handle_click(self):
        self.hide()
        if self.parent():
            self.parent().show()  # 显示父窗口


class EMinorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(EMinorWindow, self).__init__(parent)
        self.directory_selected = None  # 用于存储选择的目录
        self.another_window = None
        self.xml_or_mid = None
        self.ui = Ui_EMin()
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
            xml_save(self.directory_selected, key="E minor")  # 存为.xml文件
        elif self.xml_or_mid == "mid":
            midi_save(self.directory_selected, key="E minor")  # 存为.mid文件
        elif self.xml_or_mid == "MuseScore":
            GoMuseScore(self.directory_selected, key="E minor")  # 在MuseScore中打开乐谱

    def Go_back_handle_click(self):
        self.hide()
        if self.parent():
            self.parent().show()  # 显示父窗口


class DMinorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(DMinorWindow, self).__init__(parent)
        self.directory_selected = None  # 用于存储选择的目录
        self.another_window = None
        self.xml_or_mid = None
        self.ui = Ui_DMin()
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
            xml_save(self.directory_selected, key="D minor")  # 存为.xml文件
        elif self.xml_or_mid == "mid":
            midi_save(self.directory_selected, key="D minor")  # 存为.mid文件
        elif self.xml_or_mid == "MuseScore":
            GoMuseScore(self.directory_selected, key="D minor")  # 在MuseScore中打开乐谱

    def Go_back_handle_click(self):
        self.hide()
        if self.parent():
            self.parent().show()  # 显示父窗口


class EbMinorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(EbMinorWindow, self).__init__(parent)
        self.directory_selected = None  # 用于存储选择的目录
        self.another_window = None
        self.xml_or_mid = None
        self.ui = Ui_EbMin()
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
            xml_save(self.directory_selected, key="Eb minor")  # 存为.xml文件
        elif self.xml_or_mid == "mid":
            midi_save(self.directory_selected, key="Eb minor")  # 存为.mid文件
        elif self.xml_or_mid == "MuseScore":
            GoMuseScore(self.directory_selected, key="Eb minor")  # 在MuseScore中打开乐谱

    def Go_back_handle_click(self):
        self.hide()
        if self.parent():
            self.parent().show()  # 显示父窗口


class FMinorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(FMinorWindow, self).__init__(parent)
        self.directory_selected = None  # 用于存储选择的目录
        self.another_window = None
        self.xml_or_mid = None
        self.ui = Ui_FMin()
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
            xml_save(self.directory_selected, key="F minor")  # 存为.xml文件
        elif self.xml_or_mid == "mid":
            midi_save(self.directory_selected, key="F minor")  # 存为.mid文件
        elif self.xml_or_mid == "MuseScore":
            GoMuseScore(self.directory_selected, key="F minor")  # 在MuseScore中打开乐谱

    def Go_back_handle_click(self):
        self.hide()
        if self.parent():
            self.parent().show()  # 显示父窗口


class F_MinorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(F_MinorWindow, self).__init__(parent)
        self.directory_selected = None  # 用于存储选择的目录
        self.another_window = None
        self.xml_or_mid = None
        self.ui = Ui_F_min()
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
            xml_save(self.directory_selected, key="F# minor")  # 存为.xml文件
        elif self.xml_or_mid == "mid":
            midi_save(self.directory_selected, key="F# minor")  # 存为.mid文件
        elif self.xml_or_mid == "MuseScore":
            GoMuseScore(self.directory_selected, key="F# minor")  # 在MuseScore中打开乐谱

    def Go_back_handle_click(self):
        self.hide()
        if self.parent():
            self.parent().show()  # 显示父窗口


class GMinorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(GMinorWindow, self).__init__(parent)
        self.directory_selected = None  # 用于存储选择的目录
        self.another_window = None
        self.xml_or_mid = None
        self.ui = Ui_GMin()
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
            xml_save(self.directory_selected, key="G minor")  # 存为.xml文件
        elif self.xml_or_mid == "mid":
            midi_save(self.directory_selected, key="G minor")  # 存为.mid文件
        elif self.xml_or_mid == "MuseScore":
            GoMuseScore(self.directory_selected, key="G minor")  # 在MuseScore中打开乐谱

    def Go_back_handle_click(self):
        self.hide()
        if self.parent():
            self.parent().show()  # 显示父窗口


class AbMinorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AbMinorWindow, self).__init__(parent)
        self.directory_selected = None  # 用于存储选择的目录
        self.another_window = None
        self.xml_or_mid = None
        self.ui = Ui_AbMin()
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
            xml_save(self.directory_selected, key="Ab minor")  # 存为.xml文件
        elif self.xml_or_mid == "mid":
            midi_save(self.directory_selected, key="Ab minor")  # 存为.mid文件
        elif self.xml_or_mid == "MuseScore":
            GoMuseScore(self.directory_selected, key="Ab minor")  # 在MuseScore中打开乐谱

    def Go_back_handle_click(self):
        self.hide()
        if self.parent():
            self.parent().show()  # 显示父窗口


class AMinorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AMinorWindow, self).__init__(parent)
        self.directory_selected = None  # 用于存储选择的目录
        self.another_window = None
        self.xml_or_mid = None
        self.ui = Ui_AMin()
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
            xml_save(self.directory_selected, key="A minor")  # 存为.xml文件
        elif self.xml_or_mid == "mid":
            midi_save(self.directory_selected, key="A minor")  # 存为.mid文件
        elif self.xml_or_mid == "MuseScore":
            GoMuseScore(self.directory_selected, key="A minor")  # 在MuseScore中打开乐谱

    def Go_back_handle_click(self):
        self.hide()
        if self.parent():
            self.parent().show()  # 显示父窗口


class BbMinorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(BbMinorWindow, self).__init__(parent)
        self.directory_selected = None  # 用于存储选择的目录
        self.another_window = None
        self.xml_or_mid = None
        self.ui = Ui_BbMin()
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
            xml_save(self.directory_selected, key="Bb minor")  # 存为.xml文件
        elif self.xml_or_mid == "mid":
            midi_save(self.directory_selected, key="Bb minor")  # 存为.mid文件
        elif self.xml_or_mid == "MuseScore":
            GoMuseScore(self.directory_selected, key="Bb minor")  # 在MuseScore中打开乐谱

    def Go_back_handle_click(self):
        self.hide()
        if self.parent():
            self.parent().show()  # 显示父窗口


class BMinorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(BMinorWindow, self).__init__(parent)
        self.directory_selected = None  # 用于存储选择的目录
        self.another_window = None
        self.xml_or_mid = None
        self.ui = Ui_BMin()
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
            xml_save(self.directory_selected, key="B minor")  # 存为.xml文件
        elif self.xml_or_mid == "mid":
            midi_save(self.directory_selected, key="B minor")  # 存为.mid文件
        elif self.xml_or_mid == "MuseScore":
            GoMuseScore(self.directory_selected, key="B minor")  # 在MuseScore中打开乐谱

    def Go_back_handle_click(self):
        self.hide()
        if self.parent():
            self.parent().show()  # 显示父窗口
