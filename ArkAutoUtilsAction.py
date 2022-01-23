import os

from PyQt5.QtCore import QThread, pyqtSignal
from ArkAutoUtilesArgs import ut
class UtilsThread(QThread):
    signal_str = None
    def __init__(self):
        super(UtilsThread, self).__init__()
    def run(self) -> None:
        if self.signal_str == 'openDownBt':
            self.openDownBtThread()
        if self.signal_str == 'openWikiBt':
            self.openWikiBtThread()
    def openDownBtThread(self):
        os.system('start ./掉落图.png')
    def openWikiBtThread(self):
        os.system('start https://prts.wiki/w/%E9%A6%96%E9%A1%B5')
    def getSignal(self, text):
        self.signal_str = text
