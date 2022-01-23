#!/usr/bin/env python
# coding: utf-8
import os
import time

import win32con
import win32gui
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox

from ArkAutoAction import WorkThread
from ArkAutoUI import Ui_MainWindow
from ArkAutoUtilesArgs import ut

# from HitokotoApi import getHitokotoText

import sys


class MainUI(QMainWindow):
    MThread_Signal = pyqtSignal(str)

    def __init__(self):
        super(MainUI, self).__init__()
        self.ui = None
        self.WThread = WorkThread()
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
        self.setFixedSize(self.width(), self.height())
        # self.setWindowFlag(Qt.FramelessWindowHint)

        self.ui.expMapBt.clicked.connect(self.exp_5)
        self.ui.devConnectBt.clicked.connect(self.connectDev)
        self.ui.startGameBt.clicked.connect(self.launchGame)
        self.ui.autoFriendsBt.clicked.connect(self.autoFriend)
        self.ui.autoCountBt.clicked.connect(self.autoCount)
        self.ui.stopAllBt.clicked.connect(self.closeMainThread)
        self.ui.setTopBt.clicked.connect(self.setTopBt)
        self.ui.shutdownBt.clicked.connect(self.shutdownBt)
        self.ui.autoBuildBt.clicked.connect(self.autoBuildBt)
        self.ui.togetherBt.clicked.connect(self.togetherBt)
        self.ui.openDownBt.clicked.connect(self.openDownBt)

        self.ui.expMapBt.setStatusTip('请在首页点击 开始经验五')
        self.ui.devConnectBt.setStatusTip('连接设备 默认雷电')
        self.ui.startGameBt.setStatusTip('启动游戏至首页')
        self.ui.autoFriendsBt.setStatusTip('拜访好友基建')
        self.ui.autoCountBt.setStatusTip('战斗页面自动循环（提前开启自动代理）')
        self.ui.stopAllBt.setStatusTip('停止现有任务')
        self.ui.setTopBt.setStatusTip('窗口是否置顶')
        self.ui.logLable.setStatusTip('状态')
        self.ui.lineEdit.setStatusTip('0 清完体力（不喝药不碎石）')
        self.ui.shutdownBt.setStatusTip('弹出关机界面')
        self.ui.autoBuildBt.setStatusTip('基建换人')
        self.ui.togetherBt.setStatusTip('经验五 好友拜访 基建')
        # self.ui.openDownBt.setStatusTip('打开掉落图')
        #todo 差个商店


    def initThread(self):
        self.MThread_Signal.connect(self.WThread.getSignal)
        self.WThread.signal.connect(self.setLogLable)
        # self.signal.emit()

    def closeMainThread(self):
        try:
            if self.WThread.isRunning():
                self.setLogLable('结束任务')
            else:
                self.setLogLable('SUCCESS')
            ut.setFlagF()

        except:
            pass

    # def initHitokoto(self):
    #     self.haT.start()
    #     self.haT.sinOut.connect(self.HitokotoThread_callback)
    def setTopBt(self):
        if self.sender().isChecked():
            win32gui.SetWindowPos(self.winId(), win32con.HWND_TOPMOST, self.x() - 7, self.y(), self.width(),
                                  self.height(), win32con.SWP_SHOWWINDOW)
        else:
            win32gui.SetWindowPos(self.winId(), win32con.HWND_NOTOPMOST, self.x() - 7, self.y(), self.width(),
                                  self.height(), win32con.SWP_SHOWWINDOW)

    def startFun(self, funName):
        # f = False
        # self.ui.expMapBt.setClickable(f)
        # self.ui.devConnectBt.setClickable(f)
        # self.ui.startGameBt.setClickable(f)
        # self.ui.autoFriendsBt.setClickable(f)
        # self.ui.autoCountBt.setClickable(f)
        # self.ui.stopAllBt.clicked.connect(True)

        if not ut.isConnect() and funName != 'connectDevThread':
            self.setLogLable('请连接后重试')
            return
        if not self.WThread.isRunning():
            self.WThread.start()
        self.MThread_Signal.emit(funName)

    def connectDev(self):
        self.startFun('connectDevThread')

    def launchGame(self):
        self.startFun('launchGameThread')

    def exp_5(self):
        self.startFun('exp_5Thread')

    def autoFriend(self):
        self.startFun('autoFriendThread')

    def autoCount(self):
        try:
            autoCount = int(self.ui.lineEdit.text())
            if autoCount < 0:
                self.setLogLable('请填写正确阿拉伯数字')
                return
            self.startFun('["autoCountThread",' + str(autoCount) + ']')
        except:
            pass
    def shutdownBt(self):
        os.system('start ./WinShutdown.py')
    def autoBuildBt(self):
        self.startFun('autoBuildBt')
    def togetherBt(self):
        self.startFun('togetherBt')
    def openDownBt(self):
        self.startFun('openDownBt')
    # ------------------------------------tools-----------------------------------
    def setLogLable(self, text):
        self.ui.logLable.setText(text + '\n' + time.strftime("%H:%M:%S", time.localtime()))
    def __del__(self):
        os.system('adb kill-server')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    win32gui.SetWindowPos(ui.winId(), win32con.HWND_TOPMOST, ui.x() - 7, ui.y(), ui.width(), ui.height(),
                              win32con.SWP_SHOWWINDOW)

    sys.exit(app.exec_())
    # todo 添加置顶按钮
    # todo 调整窗口出现位置
    # todo 添加是否使用理智按钮
    # todo 刷完关机
    # todo 自动购买商店
