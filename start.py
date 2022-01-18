import time

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox

from ArknightsThread import *
from arknightsUI import Ui_MainWindow
from arknightsBaseUtils import ut

from HitokotoApi import getHitokotoText

import sys
from threading import Thread


# pyuic5 -o test.py test.ui
# pyrcct -o test.py test.qrc
isConnect = False
autoCount = 0
class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
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

#todo 引入线程池
    def initThread(self):
        self.connectDevThread = connectDevThread()
        self.launchGameThread = launchGameThread()
        self.exp_5Thread = exp_5Thread()
        self.HitokotoApiThread = HitokotoApiThread()
        self.autoFriendThread = autoFriendThread()
        self.autoCountThread = autoCountThread()

        self.connectDevThread.sinOut.connect(self.ConnectDevThread_callback)
#todo 连接槽方法 输出日志
    def closeAllThare(self):
        self.connectDevThread.quit()
        self.launchGameThread.quit()
        self.exp_5Thread.quit()
        self.HitokotoApiThread.quit()
        self.autoFriendThread.quit()
        self.autoCountThread.quit()
    def initHitokoto(self):
        self.haT.start()
        self.haT.sinOut.connect(self.HitokotoThread_callback)

    def btEven(self):
        global isConnect,autoCount
        if self.sender().text() == '连接设备':
            self.connectDevThread.start()
            self.setLogLable('正在连接')


        elif not isConnect:
            self.setLogLable('请连接后重试')
            return
        else:
            if self.sender().text() == '启动游戏':
                self.setLogLable('正在进入游戏')
                self.launchGameThread.start()
            if self.sender().text() == '开始刷本':
                self.setLogLable('正在自动exp—5')
                self.exp_5Thread.start()
            if self.sender().text() == '好友访问':
                self.setLogLable('正在好友访问')
                self.autoFriendThread.start()
            if self.sender().text() == '停止':
                self.closeAllThare()
                self.setLogLable('正在停止所有任务')
            if self.sender().text() == '自动刷本':
                try:
                    self.autoCount = int(self.ui.lineEdit.text())
                    if self.autoCount<0:
                        raise
                except:
                    self.setLogLable('请填写正确阿拉伯数字')

                self.autoCountThread.start()



    def ConnectDevThread_callback(self, inf):
        global isConnect
        if inf:
            isConnect = True
            self.setLogLable('设备已连接')
        else:
            isConnect = False
            self.setLogLable('设备未连接')

    def HitokotoThread_callback(self, inf):
        self.ui.hitokotoLable.setText(inf)

    #------------------------------------tools-----------------------------------
    def setLogLable(self, str):
        global isConnect
        if not isConnect:
            self.ui.logLable.setText('status:未连接|' + str)
        else:
            self.ui.logLable.setText('status:已连接|' + str)




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
