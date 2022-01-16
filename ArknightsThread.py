from  PyQt5.QtCore   import QThread,pyqtSignal

from HitokotoApi import getHitokotoText
from arknightsUtils import  ut
# -----------------------------------Thread-----------------------------------

def returnHome():
    #返回主页面
    if ut.img_match('bar首页'):
        ut.touchName('bar首页')
        return True
    elif ut.img_match('barhome'):
        ut.touchName('barhome')
        ut.touchName('bar首页')
        return True
    else:
        return False
def haveRealize():
        if ut.img_match('理智界面'):
            ut.touchName('理智界面x')
            if returnHome():
                print('理智已用完')
                return False
            else:
                print('理智已用完')
                return False

class exp_5Thread(QThread):
    #经验本5
    def __init__(self):
        super(exp_5Thread, self).__init__()

    def run(self):
        while True:
            if ut.img_match('主页设置按钮'):
                ut.touchName('终端')
                break
            elif self.returnHome():
                pass
            else:
                print('无法找到主页')

        ut.touchName('日常子界面')
        ut.touchName('战术演习')
        ut.touchName('ls5')
        # for i in range():
        while True:
            ut.touchName('战斗准备')
            if haveRealize():
                pass
            else:
                return
            ut.touchName('战斗准备')
            while True:
                ut.sleep()
                print('等待战斗完成')
                if ut.img_match('战斗完成'):
                    break
            ut.sleep(10)
            ut.touchName('战斗完成')

class connectDevThread(QThread):
    #连接设备
    sinOut = pyqtSignal(bool)

    def __init__(self):
        super(connectDevThread, self).__init__()

    def run(self):
        if ut.connectDev():
            self.sinOut.emit(True)
        else:
            self.sinOut.emit(False)


class launchGameThread(QThread):
    #加载游戏
    def __init__(self):
        super(launchGameThread, self).__init__()

    def run(self):
        ut.startapp('com.hypergryph.arknights')
        while True:
            if ut.img_match('加载'):
                ut.touchName('加载')
                break
            ut.sleep()
        while True:
            if ut.img_match('开始唤醒'):
                ut.touchName('开始唤醒')
                break
            ut.sleep()
        print('loading DONE')

class autoFriendThread(QThread):
    #好友拜访
    def __init__(self):
        super(autoFriendThread, self).__init__()
    def run(self) :
        if not ut.img_match('主页好友按钮'):
            if not returnHome():
                print('无法找到主页')
        else:
            ut.touchName('好友')
            ut.touchName('好友列表')
            ut.touchName('访问第一位好友')
            while True:
                if ut.img_match('下一位暗'):
                    break
                else:
                    ut.touchName('访问下一位')
            returnHome()
            print('好友访问完成')

class autoCountThread(QThread):
    def __init__(self):
        super(autoCountThread, self).__init__()
    def run(self,autoCound):
        if autoCound == 0:
            while True:
                ut.touchName('战斗准备')
        for i in range(0,autoCound + 1):
            pass





class HitokotoApiThread(QThread):
    #一言 todo内存不足
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
