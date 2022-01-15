from PyQt5.QtWidgets import  QApplication,QWidget,QMainWindow
from arknightsUI import Ui_MainWindow
import sys
from arknightsFun import fun
import threading
#pyuic5 -o test.py test.ui
class MainUI(QMainWindow):
    def __init__(self):

        super().__init__()
        self.initUI()
        self.show()


    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Arknights ADB Auto')
        self.ui.expMapBt.clicked.connect(self.expMapBt)
        self.ui.devConnectBt.clicked.connect(self.devConnectBt)

    def devConnectBt(self,bt):
        threading.Thread(target=lambda :fun.connectDev()).start()
    def expMapBt(self,bt):
        # pass
        threading.Thread(target=lambda : fun.normal()).start()

    def startGame(self,bt):
        # pass
        threading.Thread(target=lambda :fun.startGame()).start()



app = QApplication(sys.argv)
if __name__ == "__main__":
    ui = MainUI()
    sys.exit(app.exec_())
