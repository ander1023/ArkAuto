#!/usr/bin/env python
# coding: utf-8
import time

from PyQt5.QtCore import QThread, pyqtSignal

from HitokotoApi import getHitokotoText
from arknightsBaseUtils import ut


# -----------------------------------Thread-----------------------------------
class MainThread(QThread):
    signal = pyqtSignal(str)#发送
    signal_str = None#接收
    data = None
    def __init__(self):
        super(MainThread, self).__init__()

        self.flag = None
        self.battleCount = 0

    def run(self):
        time.sleep(1)  # 等待判断
        self.flag = True
        if self.signal_str == None:
            return
        if self.signal_str == 'exp_5Thread':
            self.exp_5Thread()
        if self.signal_str == 'connectDevThread':
            self.connectDevThread()

        if self.signal_str == 'launchGameThread':
            self.launchGameThread()
        if self.signal_str == 'autoFriendThread':
            self.autoFriendThread()
        if self.signal_str == 'autoCountThread':
            self.autoCountThread()

    def getSignal(self, text):
        try:
            textList = eval(text)
        except:
            textList = [text]
        if text == 'close':
            self.flag = False
        if len(textList)==1:
            self.signal_str = text
        if len(textList)>1:
            self.data =int(textList[1])
#----------------------------fun------------------------
    def exp_5Thread(self):
        self.setLogLable('经验五任务启动中..')
        while self.flag:
            if ut.img_match('主页设置按钮'):
                self.exp_5Thread_work()
                break
            elif self.returnHome():
                self.exp_5Thread_work()
            else:
                self.setLogLable('无法找到主页')
                return

    def exp_5Thread_work(self):
        ut.touchName('终端')
        ut.touchName('日常子界面')
        ut.touchName('战术演习')
        ut.touchName('ls5')
        # for i in range():
        self.onceBattleRound()
        self.setLogLable('SUCCESS')

    def connectDevThread(self):
        if ut.connectDev():
            self.setLogLable('连接成功')
        else:
            self.setLogLable('连接失败')

    def launchGameThread(self):
        self.setLogLable('启动游戏中..')
        ut.startapp('com.hypergryph.arknights')
        self.setLogLable('加载中')
        while self.flag:
            if ut.img_match('加载'):
                ut.touchName('加载')
                break
            ut.sleep()
        self.setLogLable('加载完成')
        while self.flag:
            if ut.img_match('开始唤醒'):
                ut.touchName('开始唤醒')
                break
            ut.sleep()
        self.setLogLable('SUCCESS')

    def autoFriendThread(self):
        self.setLogLable('好友任务启动中..')
        if ut.img_match('主页设置按钮'):
            self.autoFriendThread_work()
        elif self.returnHome():
            if ut.img_match('主页设置按钮'):
                self.autoFriendThread_work()
        else:
            self.setLogLable('无法找到主页')
        self.setLogLable('SUCCESS')

    def autoFriendThread_work(self):
        ut.touchName('好友')
        if not self.flag:
            return
        ut.touchName('好友列表')
        if not self.flag:
            return
        ut.touchName('访问第一位好友')
        if not self.flag:
            return
        while self.flag:
            ut.sleep(1)
            if ut.img_match('下一位暗') and self.flag:
                # todo 判断出错暂未解决
                self.returnHome()
                self.setLogLable('好友访问完成')
                return
            else:
                if not self.flag:
                    return
                self.setLogLable('访问下一位')
                ut.touchName('访问下一位')

    def autoCountThread(self):
        ac = self.data
        if ac < 0:
            return
        if ac == 0:
            self.onceBattleRound()
            return
        for i in range(1, ac + 1) :
            print(i)
            if self.flag == False:
                return
            self.setLogLable('次数：'+ str(i) + '次 还剩：'+ str(ac+1-i) + '次')
            ut.sleep()
            self.onceBattleRound()
        self.returnHome()
        self.setLogLable('SUCCESS')


    # -------------------------tool--------------------
    def enterBattle(self):
        self.setLogLable('开始行动')
        ut.touchName('战斗准备')
        if self.outRealize():
            return False
            # todo 如果outRealize方法修改 则判断没有药时为false
        ut.touchName('战斗准备1')
        return True

    def whileWaitBattleComplete(self):
        while self.flag:
            if ut.img_match('作战简报'):
                ut.touchName('剿灭完成')
                ut.sleep(5)
                self.setLogLable('剿灭完成')
            if ut.img_match('战斗完成'):
                ut.sleep(10)
                self.setLogLable('战斗完成')
                ut.touchName('战斗完成')
                return True
            ut.sleep()

    def onceBattleRound(self):
        self.setLogLable('开始副本循环')
        while self.flag:
            if self.enterBattle():
                self.setLogLable('等待战斗完成')
                self.whileWaitBattleComplete()
                return
            ut.sleep()

    def returnHome(self):
        # 返回主页面
        self.setLogLable('开始返回主页面')
        if ut.img_match('bar首页'):
            ut.touchName('bar首页')
            ut.sleep()
            return True
        elif ut.img_match('barhome'):
            ut.touchName('barhome')
            ut.touchName('bar首页')
            ut.sleep()

            return True
        else:
            return False

    def outRealize(self):
        # todo 修改参数令其使用有两种情况
        if ut.img_match('理智界面'):
            self.setLogLable('处理理智界面')
            ut.touchName('理智界面x')
            self.setLogLable('理智已用完')
            self.returnHome()
            #todo 暂定上
            return True
        return False

    def isCheckAuto(self):
        pass
    def setLogLable(self,text):
        self.signal.emit(text)


class HitokotoApiThread(QThread):
    # 一言 todo 内存不足
    sinOut = pyqtSignal(str)

    def __init__(self):
        super(HitokotoApiThread, self).__init__()

    def run(self):
        while True:
            ut.sleep(1.7)
            textStr = getHitokotoText()
            self.sinOut.emit(textStr)
            # print(textStr)
            ut.sleep(13)
