#!/usr/bin/env python
# coding: utf-8
import arknightsUtils as utils
class ADBTOOL:
    def loading(self):
        utils.ut.startapp('com.hypergryph.arknights')
        while True:
            if utils.ut.img_match('加载'):
                utils.ut.touchName('加载')
                break
            utils.ut.sleep()
        while True:
            if utils.ut.img_match('开始唤醒'):
                utils.ut.sleep()
                utils.ut.touchName('开始唤醒')
                break
            utils.ut.sleep()
        print('loading DONE')


    def normal(self):
        utils.ut.sleep()
        while True:
            if utils.ut.img_match('主页设置按钮'):
                utils.ut.touchName('终端')
                utils.ut.sleep()
                break
            elif self.returnHome():
                pass
            else:
                print('无法找到主页')

        utils.ut.touchName('日常子界面')
        utils.ut.sleep()
        utils.ut.touchName('战术演习')
        utils.ut.sleep()
        utils.ut.touchName('ls5')
        utils.ut.sleep()
        #for i in range():
        while True:
            utils.ut.touchName('战斗准备')
            utils.ut.sleep()

            if utils.ut.img_match('理智界面'):
                utils.ut.sleep()
                utils.ut.touchName('理智界面x')
                utils.ut.sleep()
                if self.returnHome():
                    print('理智已用完')
                    return
                else :
                    print('理智已用完')
                    return
            utils.ut.sleep()
            utils.ut.touchName('战斗准备')
            while True:
                utils.ut.sleep()
                print('等待战斗完成')
                if utils.ut.img_match('战斗完成'):
                    break
            utils.ut.sleep(10)
            utils.ut.touchName('战斗完成')
            utils.ut.sleep()
    def returnHome(self):
        utils.ut.sleep()
        if utils.ut.img_match('bar首页'):
            utils.ut.touchName('bar首页')
            return True
        elif utils.ut.img_match('barhome'):
            utils.ut.touchName('barhome')
            utils.ut.sleep()
            utils.ut.touchName('bar首页')
            utils.ut.sleep()
            return True
        else:
            return False


if __name__ == "__main__":
    A = ADBTOOL()
    A.loading()
    A.normal()



    #--
    # A.battleStart()
    # A.battleFinish()
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
