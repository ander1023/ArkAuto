#!/usr/bin/env python
# coding: utf-8
import time

from PyQt5.QtCore import QThread, pyqtSignal

from HitokotoApi import getHitokotoText
from arknightsBeanAndUtils import ut


# -----------------------------------Thread-----------------------------------
class WorkThread(QThread):
    signal = pyqtSignal(str)#发送
    signal_str = None#接收
    data = None
    def __init__(self):
        super(WorkThread, self).__init__()
        self.battleCount = 0

    def run(self):
        time.sleep(1)  # 等待判断
        ut.setFlagT()
        if self.signal_str == None:
            return
        self._setLogLable('任务启动中')
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
        ut.sleep(1)
        self._setLogLable('SUCCESS')

    def getSignal(self, text):
        try:
            textList = eval(text)
        except:
            textList = [text]
        if len(textList)==1:
            self.signal_str = text
        if len(textList)>1:
            self.data =int(textList[1])
#----------------------------fun------------------------
    def exp_5Thread(self):
        while ut.getFlag():
            if ut.img_match('主页设置按钮'):
                ut.touchName('终端')
                ut.touchName('日常子界面')
                ut.touchName('战术演习')
                ut.touchName('ls5')
                self._exp_5Thread_work()
                return

            elif self._returnHome():
                ut.touchName('终端')
                ut.touchName('日常子界面')
                ut.touchName('战术演习')
                ut.touchName('ls5')
                self._exp_5Thread_work()
                return
            else:
                self._setLogLable('无法找到主页')
                return

    def _exp_5Thread_work(self):
        while ut.getFlag():
            if self._enterBattle():
                self._whileWaitBattleComplete()
            else:
                self._returnHome()
                return
            ut.sleep()


    def connectDevThread(self):
        ut.connectDev()
        if ut.isConnect():
            self._setLogLable('连接成功')
        else:
            self._setLogLable('连接失败')

    def launchGameThread(self):
        ut.startapp('com.hypergryph.arknights')
        self._setLogLable('加载中')
        while ut.getFlag():
            if ut.img_match('加载'):
                ut.touchName('加载')
                break
            ut.sleep()
        self._setLogLable('加载完成')
        while ut.getFlag():
            if ut.img_match('开始唤醒'):
                ut.touchName('开始唤醒')
                break
            ut.sleep()

    def autoFriendThread(self):
        if ut.img_match('主页设置按钮'):
            self._autoFriendThread_work()
        elif self._returnHome():
            if ut.img_match('主页设置按钮'):
                self._autoFriendThread_work()
        else:
            self._setLogLable('无法找到主页')

    def _autoFriendThread_work(self):
        if not ut.getFlag():
            return
        ut.touchName('好友')
        if not ut.getFlag():
            return
        ut.touchName('好友列表')
        if not ut.getFlag():
            return
        ut.touchName('访问第一位好友')
        if not ut.getFlag():
            return
        while ut.getFlag():
            ut.sleep(1)
            if ut.img_match('下一位暗') and ut.getFlag():
                # todo 判断出错暂未解决
                self._returnHome()
                self._setLogLable('好友访问完成')
                return
            else:
                if not ut.getFlag():
                    return
                self._setLogLable('访问下一位')
                ut.touchName('访问下一位')

    def autoCountThread(self):
        ac = self.data
        if ac < 0:
            return
        if ac == 0:
            self._onceBattleRound()
            return
        for i in range(1, ac + 1) :
            if not ut.getFlag():
                return
            self._setLogLable('次数：' + str(i) + '次 还剩：' + str(ac + 1 - i) + '次')
            ut.sleep()
            self._onceBattleRound()
        self._returnHome()


    # -------------------------tool--------------------
    def _enterBattle(self):
        if not ut.getFlag():
            return
        self._setLogLable('开始行动')
        ut.touchName('战斗准备')
        if self._outRealize():
            return False
            # todo 如果outRealize方法修改 则判断没有药时为false
        ut.touchName('战斗准备1')
        return True

    def _whileWaitBattleComplete(self):
        if not ut.getFlag():
            return
        while ut.getFlag():
            if ut.img_match('作战简报'):
                ut.touchName('剿灭完成')
                ut.sleep(5)
                self._setLogLable('剿灭完成')
            if ut.img_match('战斗完成'):
                ut.sleep(10)
                self._setLogLable('战斗完成')
                ut.touchName('战斗完成')
                return True
            ut.sleep()

    def _onceBattleRound(self):
        if not ut.getFlag():
            return
        self._setLogLable('开始副本循环')
        while ut.getFlag():
            if self._enterBattle():
                self._setLogLable('等待战斗完成')
                self._whileWaitBattleComplete()
                return
            ut.sleep()

    def _returnHome(self):
        if not ut.getFlag():
            return
        # 返回主页面
        self._setLogLable('开始返回主页面')
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

    def _outRealize(self):
        if not ut.getFlag():
            return
        # todo 修改参数令其使用有两种情况
        if ut.img_match('理智界面'):
            self._setLogLable('处理理智界面')
            ut.touchName('理智界面x')
            self._setLogLable('理智已用完')
            self._returnHome()
            #todo 暂定上
            return True
        return False

    def _isCheckAuto(self):
        pass
    def _setLogLable(self, text):
        self.signal.emit(text)

#
# class HitokotoApiThread(QThread):
#     # 一言 todo 内存不足
#     sinOut = pyqtSignal(str)
#
#     def __init__(self):
#         super(HitokotoApiThread, self).__init__()
#
#     def run(self):
#         while True:
#             ut.sleep(1.7)
#             textStr = getHitokotoText()
#             self.sinOut.emit(textStr)
#             # print(textStr)
#             ut.sleep(13)
