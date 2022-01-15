import time

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
from arknightsUI import Ui_MainWindow
from arknightsUtils import ut

from HitokotoApi import getHitokotoText

import sys
from threading import Thread


# pyuic5 -o test.py test.ui
# pyrcct -o test.py test.qrc
isConnect = False
class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        self.initUI()
        self.initThread()
        self.initHitokoto()
        # self.connectThread = None,
        # self.launchGameThread = None,
        # self.exp_5Thread = None

    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Arknights by大山猛')
        self.setWindowIcon(QIcon('ui_img/icon.jpg'))
        self.ui.expMapBt.clicked.connect(self.btEven)
        self.ui.devConnectBt.clicked.connect(self.btEven)
        self.ui.startGameBt.clicked.connect(self.btEven)

    def initThread(self):
        self.cdT = connectDevThread()
        self.lgT = launchGameThread()
        self.e5T = exp_5Thread()
        self.haT = HitokotoApiThread()

    def initHitokoto(self):
        self.haT.start()
        self.haT.sinOut.connect(self.haT_changeLable)

    def btEven(self):
        global isConnect
        if self.sender().text() == '连接设备':
            self.cdT.start()
            self.ui.stateLable.setText('正在连接...')
            self.cdT.sinOut.connect(self.cdT_isConnect)
        if self.sender().text() == '启动游戏':
            if not isConnect:
                return
            self.lgT.start()
        if self.sender().text() == '开始刷本':
            if not isConnect:
                return
            self.e5T.start()

    def cdT_isConnect(self, inf):
        global isConnect
        if inf:
            self.ui.stateLable.setText("设备已连接")
            isConnect = True
        else:
            self.ui.stateLable.setText("设备未连接")
            isConnect = False

    def haT_changeLable(self, inf):
        self.ui.hitokotoLable.setText(inf)

    #------------------------------------tools-----------------------------------
    def changeLogLable(self,str):
        self.ui.logLable.setText(str)
    # -----------------------------------fun-----------------------------------
    # def launchGame(self):
    #     ut.startapp('com.hypergryph.arknights')
    #     while True:
    #         if ut.img_match('加载'):
    #             ut.touchName('加载')
    #             break
    #         ut.sleep()
    #     while True:
    #         if ut.img_match('开始唤醒'):
    #             ut.sleep(5)
    #             ut.touchName('开始唤醒')
    #             break
    #         ut.sleep()
    #     print('loading DONE')


class exp_5Thread(QThread):
    def __init__(self):
        super(exp_5Thread, self).__init__()

    def run(self):
        while True:
            if ut.img_match('主页设置按钮'):
                ut.touchName('终端')
                ut.sleep()
                break
            elif self.returnHome():
                pass
            else:
                print('无法找到主页')

        ut.touchName('日常子界面')
        ut.sleep()
        ut.touchName('战术演习')
        ut.sleep()
        ut.touchName('ls5')
        ut.sleep()
        # for i in range():
        while True:
            ut.touchName('战斗准备')
            ut.sleep()

            if ut.img_match('理智界面'):
                ut.sleep()
                ut.touchName('理智界面x')
                ut.sleep()
                if self.returnHome():
                    print('理智已用完')
                    return
                else:
                    print('理智已用完')
                    return
            ut.sleep()
            ut.touchName('战斗准备')
            while True:
                ut.sleep()
                print('等待战斗完成')
                if ut.img_match('战斗完成'):
                    break
            ut.sleep(10)
            ut.touchName('战斗完成')
            ut.sleep()

    def returnHome(self):
        ut.sleep()
        if ut.img_match('bar首页'):
            ut.touchName('bar首页')
            return True
        elif ut.img_match('barhome'):
            ut.touchName('barhome')
            ut.sleep()
            ut.touchName('bar首页')
            ut.sleep()
            return True
        else:
            return False


class connectDevThread(QThread):
    sinOut = pyqtSignal(bool)

    def __init__(self):
        super(connectDevThread, self).__init__()

    def run(self):
        if ut.connectDev():
            self.sinOut.emit(True)
        else:
            self.sinOut.emit(False)


class launchGameThread(QThread):
    def __init__(self):
        super(launchGameThread, self).__init__()

    def run(self):
        ut.startapp('com.hypergryph.arknights')
        while True:
            if ut.img_match('加载'):
                ut.touchName('加载')
                break
            ut.sleep()
        while True:
            if ut.img_match('开始唤醒'):
                ut.sleep(5)
                ut.touchName('开始唤醒')
                break
            ut.sleep()
        print('loading DONE')


class HitokotoApiThread(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self):
        super(HitokotoApiThread, self).__init__()

    def run(self):
        while True:
            time.sleep(1.7)
            textStr = getHitokotoText()
            self.sinOut.emit(textStr)
            # print(textStr)
            ut.sleep(13)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    # ui.setWindowFlags(Qt.WindowCloseButtonHint)

    ui.setFixedSize(ui.width(), ui.height())
    ui.show()
    sys.exit(app.exec_())
