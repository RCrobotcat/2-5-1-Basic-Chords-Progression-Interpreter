from PySide6.QtWidgets import QApplication, QMainWindow
from window_main import Ui_Interpreter_main
from ui_setKeys import Ui_setKeys
from PySide6.QtCore import QCoreApplication
import majorKeys
import minorKeys
from window_WIP import Ui_wip

# PySide6-uic Fminor.ui -o window_Fminor.py
# pyside6-rcc -o image_1_rc.py image_1.qrc


def quit_progress():
    QCoreApplication.instance().quit()  # 程序退出

class WIPWindow(QMainWindow):
    def __init__(self, parent=None):
        super(WIPWindow, self).__init__(parent)
        self.ui = Ui_wip()
        self.ui.setupUi(self)
        self.bind()

    def bind(self):
        self.ui.BackButton.clicked.connect(self.Go_back_handle_click)

    def Go_back_handle_click(self):
        self.hide()
        self.parent().show()  # 显示父窗口

class SetKeysWindow(QMainWindow):
    def __init__(self, parent=None):
        super(SetKeysWindow, self).__init__(parent)
        self.another_window = None
        self.ui = Ui_setKeys()
        self.ui.setupUi(self)
        self.bind()

    def bind(self):
        self.ui.Cmaj.clicked.connect(self.handle_click_cMaj)
        self.ui.Dbmaj.clicked.connect(self.handle_click_DbMaj)
        self.ui.Dmaj.clicked.connect(self.handle_click_DMaj)
        self.ui.Ebmaj.clicked.connect(self.handle_click_EbMaj)
        self.ui.Emaj.clicked.connect(self.handle_click_EMaj)
        self.ui.Fmaj.clicked.connect(self.handle_click_FMaj)
        self.ui.F_sharp_maj.clicked.connect(self.handle_click_F_Maj)
        self.ui.Gmaj.clicked.connect(self.handle_click_GMaj)
        self.ui.Abmaj.clicked.connect(self.handle_click_AbMaj)
        self.ui.Amaj.clicked.connect(self.handle_click_AMaj)
        self.ui.Bbmaj.clicked.connect(self.handle_click_BbMaj)
        self.ui.Bmaj.clicked.connect(self.handle_click_BMaj)

        self.ui.Cm.clicked.connect(self.handle_click_CMin)
        self.ui.Dbm.clicked.connect(self.handle_click_DbMin)
        self.ui.Dm.clicked.connect(self.handle_click_DMin)
        self.ui.Ebm.clicked.connect(self.handle_click_EbMin)
        self.ui.Em.clicked.connect(self.handle_click_EMin)
        self.ui.Fm.clicked.connect(self.handle_click_FMin)
        self.ui.F_sharp_m.clicked.connect(self.handle_click_F_Min)
        self.ui.Gm.clicked.connect(self.handle_click_GMin)
        self.ui.Abm.clicked.connect(self.handle_click_AbMin)
        self.ui.Am.clicked.connect(self.handle_click_AMin)
        self.ui.Bbm.clicked.connect(self.handle_click_BbMin)
        self.ui.Bm.clicked.connect(self.handle_click_BMin)

        self.ui.toolButton.clicked.connect(self.Others_handle_click)
        self.ui.BackButton.clicked.connect(self.Go_back_handle_click)

    def handle_click_cMaj(self):
        self.another_window = majorKeys.CMajorWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

    def handle_click_DbMaj(self):
        self.another_window = majorKeys.DbMajorWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

    def handle_click_DMaj(self):
        self.another_window = majorKeys.DMajorWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

    def handle_click_EbMaj(self):
        self.another_window = majorKeys.EbMajorWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

    def handle_click_EMaj(self):
        self.another_window = majorKeys.EMajorWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

    def handle_click_FMaj(self):
        self.another_window = majorKeys.FMajorWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

    def handle_click_F_Maj(self):
        self.another_window = majorKeys.F_MajorWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

    def handle_click_GMaj(self):
        self.another_window = majorKeys.GMajorWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

    def handle_click_AbMaj(self):
        self.another_window = majorKeys.AbMajorWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

    def handle_click_AMaj(self):
        self.another_window = majorKeys.AMajorWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

    def handle_click_BbMaj(self):
        self.another_window = majorKeys.BbMajorWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

    def handle_click_BMaj(self):
        self.another_window = majorKeys.BMajorWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

    def handle_click_CMin(self):
        self.another_window = minorKeys.CMinorWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

    def handle_click_DbMin(self):
        self.another_window = minorKeys.DbMinorWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

    def handle_click_DMin(self):
        self.another_window = minorKeys.DMinorWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

    def handle_click_EMin(self):
        self.another_window = minorKeys.EMinorWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

    def handle_click_EbMin(self):
        self.another_window = minorKeys.EbMinorWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

    def handle_click_FMin(self):
        self.another_window = minorKeys.FMinorWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

    def handle_click_F_Min(self):
        self.another_window = minorKeys.F_MinorWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

    def handle_click_GMin(self):
        self.another_window = minorKeys.GMinorWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

    def handle_click_AbMin(self):
        self.another_window = minorKeys.AbMinorWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

    def handle_click_AMin(self):
        self.another_window = minorKeys.AMinorWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

    def handle_click_BbMin(self):
        self.another_window = minorKeys.BbMinorWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

    def handle_click_BMin(self):
        self.another_window = minorKeys.BMinorWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口

    def Others_handle_click(self):
        self.another_window = WIPWindow(self)
        self.another_window.show()  # 显示另一个窗口

    def Go_back_handle_click(self):
        self.hide()
        self.parent().show()  # 显示父窗口


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.another_window = None
        self.ui = Ui_Interpreter_main()
        self.ui.setupUi(self)
        self.bind()


    def bind(self):
        self.ui.startButton.clicked.connect(self.handle_click)
        self.ui.quitButton.clicked.connect(quit_progress)

    def handle_click(self):
        self.another_window = SetKeysWindow(self)
        self.hide()  # 隐藏当前窗口
        self.another_window.show()  # 显示另一个窗口


if __name__ == '__main__':
    app = QApplication([])  # 启动一个应用
    window = MainWindow()  # 实例化主窗口
    window.show()
    app.exec()  # 进入程序的主循环，等待事件
