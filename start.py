import time

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox

from ArknightsThread import *
from arknightsUI import Ui_MainWindow

from HitokotoApi import getHitokotoText

import sys


class MainUI(QMainWindow):
    MThread_Signal = pyqtSignal(str)
    def __init__(self):
        super(MainUI, self).__init__()
        self.MThread = MainThread()
        self.isConnect = False
        self.initUI()
        self.initThread()
        #self.initHitokoto()
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
        self.ui.autoFriendsBt.clicked.connect(self.btEven)
        self.ui.autoCountBt.clicked.connect(self.btEven)
        self.ui.stopAllBt.clicked.connect(self.btEven)


    def initThread(self):
        self.MThread_Signal.connect(self.MThread.getSignal)
        self.MThread.signal.connect(self.setLogLable)
        # self.signal.emit()

#todo 连接槽方法 输出日志
    def closeMainThread(self):
        if self.MThread.isRunning():
            print('MThreadisrun')
            self.MThread_Signal.emit('close')
    def initHitokoto(self):
        self.haT.start()
        self.haT.sinOut.connect(self.HitokotoThread_callback)

    def btEven(self):
        if self.sender().text() == '连接设备':
            self.setLogLable('正在连接')
            self.MThread.start()
            self.MThread_Signal.emit('connectDevThread')
        elif not self.isConnect:
            self.setLogLable('请连接后重试')
            return
        else:
            self.MThread.start()
            self.MThreadFlag = True
            if self.sender().text() == '启动游戏':
                self.setLogLable('正在进入游戏')
                self.MThread_Signal.emit('launchGameThread')
            if self.sender().text() == '开始刷本':
                self.MThread_Signal.emit('exp_5Thread')
            if self.sender().text() == '好友访问':
                self.MThread_Signal.emit('autoFriendThread')
            if self.sender().text() == '停止':
                self.closeMainThread()
            if self.sender().text() == '自动刷本':
                try:
                    self.autoCount = int(self.ui.lineEdit.text())
                    if self.autoCount<0:
                        raise
                except:
                    self.setLogLable('请填写正确阿拉伯数字')

                self.MThread_Signal.emit('autoCountThread')

    #------------------------------------tools-----------------------------------
    def setLogLable(self, text):
        if text == '连接成功':
            self.isConnect = True
            return
        if not self.isConnect:
            self.ui.logLable.setText('status:未连接| 运行失败')
        else:
            self.ui.logLable.setText('status:已连接| ' + text)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ui = MainUI()
    ui.setFixedSize(ui.width(), ui.height())
    ui.setWindowFlags(Qt.WindowStaysOnTopHint)
    ui.show()
    sys.exit(app.exec_())
    #todo 添加置顶按钮
    #todo 调整窗口出现位置
    #todo 添加是否使用理智按钮
    #todo 刷完关机
    #todo 自动购买商店
