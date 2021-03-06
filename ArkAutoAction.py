#!/usr/bin/env python
# coding: utf-8
import os
import time

from PyQt5.QtCore import QThread, pyqtSignal

# from HitokotoApi import getHitokotoText
from ArkAutoUtilesArgs import ut

# -----------------------------------Thread-----------------------------------
class WorkThread(QThread):
    signal = pyqtSignal(str)  # 发送
    signal_str = None  # 接收
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
        if self.signal_str == 'autoBuildBt':
            self.autoBuildThread()
        if self.signal_str == 'openDownBt':
            self.openDownBtThread()
        if self.signal_str == 'togetherBt':
            self.exp_5Thread()
            ut.sleep(5)
            self.autoFriendThread()
            ut.sleep(5)
            self.autoBuildThread()




        time.sleep(1)
        self._setLogLable('SUCCESS')

    def getSignal(self, text):
        self.signal_str = None
        self.data = -1
        try:
            textList = eval(text)
        except:
            textList = [text]
        if len(textList) == 1:
            self.signal_str = text
        if len(textList) > 1:
            self.signal_str = textList[0]
            self.data = int(textList[1])

    # ----------------------------fun------------------------
    def exp_5Thread(self):
        while ut.getFlag():
            if ut.img_match('主页设置按钮'):
                self._touch('终端')
                self._touch('日常子界面')
                self._touch('战术演习')
                self._touch('LS_5')
                self._exp_5Thread_work()
                return

            elif self._returnHome():
                self._touch('终端')
                self._touch('日常子界面')
                self._touch('战术演习')
                self._touch('LS_5')
                self._exp_5Thread_work()
                return
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
                self._touch('加载')
                break
            ut.sleep()
        while ut.getFlag():
            if ut.img_match('开始唤醒'):
                self._touch('开始唤醒')
                break
            ut.sleep()

    def autoFriendThread(self):
        if ut.img_match('主页好友按钮'):
            self._autoFriendThread_work()
            return
        elif self._returnHome():
            if ut.img_match('主页设置按钮'):
                self._autoFriendThread_work()
            return
        self._setLogLable('无法找到主页')

    def _autoFriendThread_work(self):
        self._touch('好友')
        self._touch('好友列表')
        self._touch('访问第一位好友')
        while ut.getFlag():
            ut.sleep(1)

            if ut.img_match('下一位亮'):
                # 已解决 路径出错 & 灰度图片对比
                self._touch('访问下一位')
                ut.sleep(3)
            else:
                self._returnHome()
                self._setLogLable('好友访问完成')
                return

    def autoCountThread(self):
        ac = self.data
        if ac < 0:
            return
        if ac == 0:
            while ut.getFlag():
                if self._enterBattle():
                    self._whileWaitBattleComplete()
                else:
                    self._returnHome()
                    return
                ut.sleep(10)
        for i in range(1, ac + 1):
            if not ut.getFlag():
                return
            self._setLogLable('次数：' + str(i) + '次 还剩：' + str(ac + 1 - i) + '次')
            ut.sleep(5)
            if self._enterBattle():
                self._whileWaitBattleComplete()
            else:
                break
        self._returnHome()
    def autoBuildThread(self):
        #todo 所有发电站，第一个贸易站、交易站需要自定位置（other person）修改

        if ut.img_match('主页设置按钮'):
            self._touch('首页基建')
            #处理通知
            ut.sleep()
            if ut.img_match('蓝色通知1'):
                self._touch('蓝色通知1')
            elif ut.img_match('蓝色通知2'):
                self._touch('蓝色通知2')
            while ut.getFlag():
                if ut.img_match('可收获') or ut.img_match('可交付') or ut.img_match('收取信赖'):
                    self._touch('底部通知')
                else:
                    break
                ut.sleep()
            self._touch('返回')
            if ut.img_match('基建确认退出'):
                self._touch('基建确认退出')
                ut.sleep(5)
                self._touch('首页基建')
            #开始任务宿舍
            if ut.img_match('第一个宿舍'):
                self._touch('宿舍1')
                self._autoBuildHostelWork()
                self._touch('宿舍2')
                self._autoBuildHostelWork()
                self._touch('宿舍3')
                self._autoBuildHostelWork()
                self._touch('宿舍4')
                self._autoBuildHostelWork()
            else:
                self._setLogLable('不在基建内')
                ut.sleep()
                return
            #开始控制中枢
            ut.sleep()
            if not ut.img_match('第一个宿舍'):
                self._setLogLable('任务出错')
                ut.sleep()
                return
            self._touch('控制中枢')
            self._autoBuildHostelWork()
            #开始办公室
            self._touch('办公室')
            self._autoBuildHostelWork(1)
            #开始会客室
            self._touch('会客室')
            self._autoBuildHostelWork(2)


            #开始贸易站
            ut.sleep()
            if not ut.img_match('第一个宿舍'):
                self._setLogLable('任务出错')
                ut.sleep()
                return
            self._touch('贸易站')
            self._touch('查看订单')
            self._autoBuildDealWork()
            self._touch('列表2')
            self._autoBuildDealWork()
            self._touch('列表3')
            self._autoBuildDealWork()
            self._touchFast('返回')
            self._touchFast('返回')
            #开始制造站
            ut.sleep()
            if not ut.img_match('第一个宿舍'):
                self._setLogLable('任务出错')
                ut.sleep()
                return
            self._touch('制造站')
            self._touch('查看订单')
            self._autoBuildDealWork()
            self._touch('列表2')
            self._autoBuildDealWork()
            self._touch('列表3')
            self._autoBuildDealWork()
            self._touchFast('返回')
            self._touchFast('返回')
            #开始发电站
            ut.sleep()
            if not ut.img_match('第一个宿舍'):
                self._setLogLable('任务出错')
                ut.sleep()
                return
            self._touch('发电站1')
            self._autoBuildHostelWork(1)
            self._touch('发电站2')
            self._autoBuildHostelWork(1)
            self._touch('发电站3')
            self._autoBuildHostelWork(1)
            #结束
            self._touchFast('返回')
            if ut.img_match('基建确认退出'):
                    self._touch('基建确认退出')

        else:
            if self._returnHome():
                ut.sleep(5)
                self.autoBuildThread()
            else:
                self._setLogLable('找不到主页')
                ut.sleep()
                return
    def _autoBuildHostelWork(self, len = 5):
        if ut.img_match('进驻信息清空'):
            self._touchFast('清空')
        else:
            self._touchFast('进驻信息')
            self._touchFast('清空')
        if ut.img_match('基建确认退出'):
            self._touchFast('基建确认退出')#是否换下有体力的干员 是
        self._touch('进驻')
        if len == 1:
            self._touchFast('位置1')
        elif len == 2:
            self._touchFast('位置1')
            self._touchFast('位置2')
        elif len == 3:
            self._touchFast('位置1')
            self._touchFast('位置2')
            self._touchFast('位置3')
        elif len == 5:
            self._touchFast('位置1')
            self._touchFast('位置2')
            self._touchFast('位置3')
            self._touchFast('位置4')
            self._touchFast('位置5')
        self._touch('确认')
        if ut.img_match('排班替换提示'):
            self._touch('排班替换确认')
        self._touch('返回')
    def _autoBuildDealWork(self):
        self._touch('人员')
        self._touch('清空选择')
        self._touch('确认')
        self._touch('人员')
        self._touchFast('位置1')
        self._touchFast('位置2')
        self._touchFast('位置3')
        self._touch('确认')
        if ut.img_match('排班替换提示'):
            self._touch('排班替换确认')

    # -------------------------tool--------------------
    def _touch(self,name):
        if not ut.getFlag():
            return
        self._setLogLable(name)
        ut.touchName(name)
    def _touchFast(self,name):
        if not ut.getFlag():
            return
        self._setLogLable(name)
        ut.touchNameFast(name)
    def _enterBattle(self):
        self._isCheckAuto()
        self._touch('战斗准备')
        if self._outRealize():
            return False
            # todo 如果outRealize方法修改 则判断没有药时为false
        self._touch('战斗准备1')
        return True

    def _whileWaitBattleComplete(self):
        self._setLogLable('等待战斗结束')
        while ut.getFlag():
            if ut.img_match('作战简报'):
                self._touch('剿灭完成')
                ut.sleep(5)
            if ut.img_match('战斗完成'):
                ut.sleep(5)
                self._touch('战斗完成')
                return True
            ut.sleep()

    def _returnHome(self):
        # 返回主页面
        self._setLogLable('开始返回主页面')
        if ut.img_match('bar首页'):
            self._touch('bar首页')
            if ut.img_match('基建确认退出'):
                self._touch('基建确认退出')
            return True
        elif ut.img_match('barhome'):
            self._touch('barhome')
            self._touch('bar首页')
            if ut.img_match('基建确认退出'):
                self._touch('基建确认退出')
            return True
        return False

    def _outRealize(self):
        # todo 修改参数令其使用有两种情况
        # 嗑了我两颗石头！！！！！！！！
        # todo 源石嗑药界面
        if ut.img_match('理智界面') or ut.img_match('源石理智界面'):
            self._setLogLable('处理理智界面')
            self._touch('理智界面x')
            self._setLogLable('理智已用完')
            # todo 暂定上
            return True
        return False

    def _isCheckAuto(self):
        if ut.img_match('代理指挥'):
            pass
        else:
            pass
            # self._touch('代理指挥')

    def _setLogLable(self, text):
        if text != 'SUCCESS' and not ut.getFlag():
            return
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
