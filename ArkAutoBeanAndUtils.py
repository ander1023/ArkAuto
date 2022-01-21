#!/usr/bin/env python
# coding: utf-8
import os

from airtest.aircv import crop_image
from airtest.core.android.android import Android
from airtest.core.api import *
import time
import random


# todo 修改为本地日志
class Utils:
    IM = {
        # load
        '加载': ['game_img/tpl1642000237225.png', [1200, 10, 1260, 85]],
        '开始唤醒': ['game_img/tpl1642001226694.png', [530, 476, 740, 544]],
        # main
        '主页设置按钮': ['game_img/tpl1642001430437.png', [17, 17, 86, 64]],
        '主页好友按钮': ['game_img/tpl1642224008220.png', [294, 550, 427, 587]],
        '主页采购中心': ['game_img/tpl1642222433924.png', [752, 453, 917, 524]],
        # 商店界面
        '收取信用': ['game_img/tpl164222,2452232.png', [956, 15, 1083, 50]],
        # 好友界面
        '下一位亮':['game_img/tpl1642695536661.png',[1115,579,1264,610]],
        '下一位暗': ['game_img/tpl1642316165139.png', [1089, 578, 1277, 680]],
        # battle
        '战斗完成': ['game_img/tpl1642146871581.png', [23, 574, 400, 676]],
        '理智界面': ['game_img/tpl1642165866975.png.', [1099, 383, 1225, 409]],
        '源石理智界面':['game_img/tpl1642671953935.png',[709,233,877,408]],
        '代理指挥':['game_img/tpl1642696553627.png',[900,627,960,675]],
        # bar
        'barhome': ['game_img/tpl1642147290374.png', [165, 14, 376, 67]],
        'bar首页': ['game_img/tpl1642147630815.png', [34, 221, 129, 310]],
        # 剿灭
        '作战简报': ['game_img/tpl1642436676650.png', [73, 173, 196, 213]],
        #基建
        '基建确认退出':['game_img/tpl1642744849275.png',[ 800,470,880,560]],
        '第一个宿舍' :['game_img/tpl1642744834921.png',[660,260,760,300]],
        '蓝色通知1' :['game_img/tpl1642744906228.png',[1170,73,1230,105]],
        '蓝色通知2' :['game_img/tpl1642744906228.png',[1170,115,1220,160]],
        '可收获' :['game_img/tpl1642746869166.png',[155,640,207,700]],
        '可交付' :['game_img/tpl1642747468444.png',[155,640,207,700]],
        '收取信赖':['game_img/tpl1642780458519.png',[155,640,207,700]],
        '进驻信息清空':['game_img/tpl1642747239480.png',[1150,4,1246,53]],
        '排班替换提示':['game_img/tpl1642749701931.png',[930,660,1007,690]]
    }
    CM = {
        # clickmap
        # load
        '加载': [200, 500],
        '开始唤醒': [621, 508],
        # battle
        '战斗准备': [1100, 640],
        '战斗准备1': [1100, 600],
        '战斗完成': [900, 15],
        # main
        '终端': [966, 181],
        '好友': [357, 567],
        '采购中心': [836, 477],
        # 好友界面
        '好友列表': [119, 213],
        '访问第一位好友': [994, 155],
        '访问下一位': [1194, 631],
        # 商店界面
        '信用交易所': [1194, 100],
        '领取信用': [1011, 38],
        '领取信用确定按钮': [],
        # battle 中途
        '日常子界面': [725, 669],
        '战术演习': [622, 341],
        'LS_5': [943, 177],
        '理智界面x': [779, 571],
        '代理指挥':[1136,585],
        # bar
        'barhome': [254, 29],
        'bar首页': [93, 271],
        # 剿灭完成
        '剿灭完成': [959, 120],

        #基建操作
        '首页基建':	[1040,630],
        '基建确认退出':[850,520],
        '蓝色通知1':[1220,95],
        '蓝色通知2':[1200,130],
        '控制中枢' :[820,200],
        '宿舍1' :[820,300],
        '宿舍2' :[820,410],
        '宿舍3' :[820,510],
        '宿舍4' :[820,610],
        '贸易站':[65,300],
        '制造站':[300,300],
        '发电站1':[430,300],
        '发电站2':[430,400],
        '发电站3':[430,500],
        '会客室':[1200,200],
        '办公室':[1255,400],
        '底部通知':[222,683],
        #宿舍
        '进驻信息': [70,270],
        '清空': [1200,25],
        '进驻':[1036,140],
        '位置1':[490,200],
        '位置2':[490,460],
        '位置3':[626,200],
        '位置4':[626,460],
        '位置5':[782,200],
        '确认':[1200,640],
        '返回':[60,30],
        '排班替换确认':[1000,680],

        #贸易站&制造
        '查看订单':[350,620],
        '人员':[310,640],
        '清空选择':[500,670],
        #>确认 人员 位置1，2，3》确认
        '列表2':[110,280],
        '列表3':[110,370]
    }

    def __init__(self):
        self._dev = None
        self.flag = False
    def connectDev(self):
        try:
            os.system('adb devices')
            self._dev = Android('emulator-5554')
            # print(self._dev.get_default_device())
        except:
            pass

    # def getdev(self):
    #     return self.__dev
    def startapp(self, name):
        if not self.flag:
            return
        self._dev.start_app(name, activity=None)

    def sleep(self, second=3):
        if not self.flag:
            return
        time.sleep(second + random.random() * 2)

    def touchName(self, name):
        if not self.isConnect():
            return
        if not self.flag:
            return
        x = self.CM[name][0]
        y = self.CM[name][1]
        self._dev.touch((x, y), 0.01)
        print('touchList ' + '--' + name + '--')
        self.sleep(3)
    def touchNameFast(self, name):
        if not self.isConnect():
            return
        if not self.flag:
            return
        x = self.CM[name][0]
        y = self.CM[name][1]
        self._dev.touch((x, y), 0.01)
        print('touchList ' + '--' + name + '--')
        time.sleep(1)
    def img_match(self, name):
        if not self.isConnect():
            return
        if not self.flag:
            return
        try:
            img = self.IM[name][1]
            local_screen = crop_image(self._dev.snapshot(), (img[0], img[1], img[2], img[3]))
            tempalte = Template(self.IM[name][0])
            pos = tempalte.match_in(local_screen)
            if pos:
                print('img_match ' + '--' + name + '--  Success')
                return True
            else:
                print('img_match ' + '--' + name + '--  Fail')
                return False
        except:
            print('img_match ' + '--' + name + '--  Fail')
            return False
        finally:
            time.sleep(0.7)

    def getFlag(self):
        return self.flag
    def setFlagF(self):
        self.flag = False

    def setFlagT(self):
        self.flag = True

    def isConnect(self):
        try:
            if self._dev.get_default_device():
                return True
            return False
        except:
            pass


ut = Utils()
