from PyQt5.QtWidgets import QMainWindow
from arknightsUI import Ui_MainWindow

class mainUI(QMainWindow,):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    ui = mainUI()
    ui.show()
