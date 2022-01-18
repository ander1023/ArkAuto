from  PyQt5.QtCore   import QThread,pyqtSignal

import start
from HitokotoApi import getHitokotoText
from arknightsBaseUtils import  ut
# -----------------------------------Thread-----------------------------------


class Funtools:
    def enterBattle(self):
        ut.touchName('战斗准备')
        if self.outRealize():
            return  False
            #todo 如果outRealize方法修改 则判断没有药时为false
        ut.touchName('战斗准备1')
        return True
    def whileBattleComplete(self):
        while True:

            print('判断中')
            if ut.img_match('作战简报'):
                ut.touchName('剿灭完成')
                ut.sleep(5)
            if ut.img_match('战斗完成'):
                ut.sleep(10)
                ut.touchName('战斗完成')
                return True
            ut.sleep()
    def whileBattleRound(self):
        while True:
            if self.enterBattle():
                self.whileBattleComplete()
            else:
                break
            ut.sleep()
    def returnHome(self):
        #返回主页面
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
        #todo 修改参数令其使用有两种情况
            if ut.img_match('理智界面'):
                ut.touchName('理智界面x')
                funtools.returnHome()
                print('理智已用完')
                return True
            return False
    def isCheckAuto(self):
        pass
class exp_5Thread(QThread):
    #经验本5
    def __init__(self):
        super(exp_5Thread, self).__init__()

    def run(self):
        while True:
            if ut.img_match('主页设置按钮'):
                self.work()
                break
            elif funtools.returnHome():
                self.work()
            else:
                print('无法找到主页')
                return
    def work(self):
        ut.touchName('终端')
        ut.touchName('日常子界面')
        ut.touchName('战术演习')
        ut.touchName('ls5')
        # for i in range():
        funtools.whileBattleRound()
funtools = Funtools()
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
        if ut.img_match('主页设置按钮'):
            self.work()
        if not funtools.returnHome():
            print('无法找到主页')
            return
        elif ut.img_match('主页设置按钮'):
            self.work()
    def work(self):
        ut.touchName('好友')
        ut.touchName('好友列表')
        ut.touchName('访问第一位好友')
        while True:
            ut.sleep(1)
            if ut.img_match('下一位暗'):
                #todo 判断出错暂未解决
                funtools.returnHome()
                print('好友访问完成')
            else:
                ut.touchName('访问下一位')



class autoCountThread(QThread):
    #需要放到战斗准备界面开启代理
    def __init__(self):
        super(autoCountThread, self).__init__()
    def run(self):
        ac = start.autoCount
        #todo 获取不到数据
        if ac == 0:
           funtools.whileBattleRound()
        for i in range(1,ac+1):
            funtools.whileBattleRound()
        funtools.returnHome()





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
