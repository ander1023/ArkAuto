#!/usr/bin/env python
# coding: utf-8
import win32con
import win32gui
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
        self.ui = None
        self.MThread = MainThread()
        self.isConnect = False
        self.initUI()
        self.initThread()
        # self.initHitokoto()
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
        self.ui.setTopBt.clicked.connect(self.setTopBt)
    def initThread(self):
        self.MThread_Signal.connect(self.MThread.getSignal)
        self.MThread.signal.connect(self.setLogLable)
        # self.signal.emit()

    def closeMainThread(self):
        if self.MThread.isRunning():
            self.MThread_Signal.emit('close')
            self.setLogLable('结束任务')
            try:
                self.MThread.quit()
                self.MThread.wait()
            except:
                pass

    # def initHitokoto(self):
    #     self.haT.start()
    #     self.haT.sinOut.connect(self.HitokotoThread_callback)
    def setTopBt(self):
        if self.sender().isChecked():
            win32gui.SetWindowPos(self.winId(),win32con.HWND_TOPMOST,self.x()-7,self.y(),self.width(),self.height(),win32con.SWP_SHOWWINDOW)
        else:
            win32gui.SetWindowPos(self.winId(),win32con.HWND_NOTOPMOST,self.x()-7,self.y(),self.width(),self.height(),win32con.SWP_SHOWWINDOW)

    def btEven(self):
        if not self.MThread.isRunning():
            self.MThread.start()
        if self.sender().text() == '连接设备':
            self.MThread_Signal.emit('connectDevThread')
        elif not self.isConnect:
            self.setLogLable('请连接后重试')
            return
        else:
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
                autoCount = -1
                try:
                    autoCount = int(self.ui.lineEdit.text())

                    if autoCount < 0:
                        self.setLogLable('请填写正确阿拉伯数字')
                        return
                    self.MThread_Signal.emit('["autoCountThread",'+str(autoCount)+']')
                except:
                    pass
                    # self.setLogLable('请填写正确阿拉伯数字')
                self.MThread_Signal.emit('autoCountThread')


    # ------------------------------------tools-----------------------------------
    def setLogLable(self, text):
        if text == '连接成功':
            self.isConnect = True
        if not self.isConnect:
            self.ui.logLable.setText('status:未连接| 运行失败'+'\n'+time.strftime("%H:%M:%S", time.localtime()))
        else:
            self.ui.logLable.setText('status:已连接| ' + text+'\n'+time.strftime("%H:%M:%S", time.localtime()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.setFixedSize(ui.width(), ui.height())
    # ui.setWindowFlags(Qt.WindowStaysOnTopHint)
    ui.show()
    sys.exit(app.exec_())
    # todo 添加置顶按钮
    # todo 调整窗口出现位置
    # todo 添加是否使用理智按钮
    # todo 刷完关机
    # todo 自动购买商店
