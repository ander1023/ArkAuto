#!/usr/bin/env python
# coding: utf-8
from airtest.aircv import crop_image
from airtest.core.android.android import Android
from airtest.core.api import *
import time

IM = {
    #'加载': ['img/tpl1642000237225.png', [1200, 10, 1260, 85]],
    #'开始唤醒': ['img/tpl1642001226694.png', [530, 476, 740, 544]],
    #'主页设置按钮': ['img/tpl1642001430437.png', [17, 17, 86, 64]]
}
CM = {
    # clickmap
    #'加载': [200, 500],
    #'开始唤醒': [621, 508],
    #'战斗准备': [1100, 630],
    #'战斗完成': [900, 15]
    '现实邀约':[260,618],
    '地域':[240,646],
    '筛选':[1123,49],
    '收藏':[1220,571],
    'one':[1115,260],
    'two':[1115,415],
    'three':[1115,570],
    'switch_s':[406,288],
    'switch_end':[150,293],
    'battle':[1148,534],
    '准备':[1173,589],
    '完成':[872,520],
    '关闭':[1148,71]





}


def TW(data):
    time.sleep(data)


class ADBTOOL:
    def __init__(self):
        self.air = None
        arknights = 'com.hypergryph.arknights'
        # os.system('start leidian')
        self.air = Android('emulator-5554')
        # self.air.start_app(arknights, activity=None)
        # TW(10)
        # 等待加载
        print('init DONE')

    def normal(self):
        A.touchList('现实邀约')
        TW(10)
        A.touchList('地域')
        TW(10)
        for i in ['two','three']:
            A.touchList('筛选')
            TW(3)
            A.touchList('收藏')
            TW(3)
            A.touchList(i)
            TW(3)
            if i == 'one':
                A.air.swipe(CM['switch_s'],CM['switch_end'],duration=3)
            TW(3)
            A.touchList('battle')
            TW(12)
            A.touchList('准备')
            TW(30)
            A.touchList('完成')
            TW(10)
            A.touchList('完成')
            TW(10)
            A.touchList('关闭')
            TW(10)


    def img_match(self, data):
        # data = str im中的key
        try:
            screen = self.air.snapshot()
            img = IM[data][1]
            local_screen = crop_image(screen, (img[0], img[1], img[2], img[3]))
            tempalte = Template(IM[data][0])
            pos = tempalte.match_in(local_screen)
            print('img_match DONE')
            if pos:
                return True
            else:
                return False
        except:
            return False

    def touchList(self, data):

        # data = CM中的key
        x = CM[data][0]
        y = CM[data][1]
        self.air.touch((x, y), 0.01)
        print('touchList DONE' +'-- '+data+'-- ' )



if __name__ == "__main__":
    A = ADBTOOL()
    A.normal()

    # A.loading()
    # A.battleStart()
    # A.battleFinish()
    # print(A.img_match('主页设置按钮'))




'''
    '现实邀约':[260,618],
    '地域':[240,646],
    '筛选':[1123,49],
    '收藏':[1220,571],
    'one':[1115,260],
    'two':[1115,415],
    'three':[1115,570],
    'switch_s':[406,288],
    'switch_end':[150,293],
    'battle':[1148,259]
'''
# # 框架
# ```
# todo list
#     qtUI导入
#     文字识别
#     环境自启动
#     配置文件记录
# ```
# ## 功能设定
# ```
#     选择资源关卡自动导航
#     选择几次
#     自动选勾代理
#     界面显示资源表 wiki
#     基建
#
#
#
# ```
# ## 代码逻辑
# ```
#     adb与模拟器
#     位置与图片识别
#     返回主界面
#
# ```
