# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ArkAutoUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(392, 256)
        MainWindow.setStyleSheet("*{\n"
"font-family: \"Microsoft YaHei\";\n"
"font-weight:bold;\n"
"font-size:14px;\n"
"}\n"
"QWidget{\n"
"background:#99ccff\n"
"}\n"
"\n"
"QLabel{\n"
"color:#fff;\n"
"background:transparent;\n"
"font-size:14px;\n"
"font-weight:bold\n"
"}\n"
"\n"
"QPushButton,QCheckBox,Qmenu{\n"
"border-image:none;\n"
"border:2px solid rgba(255,255,255,0.4);\n"
"background:rgba(255,255,255,0.7);\n"
"height:30px;\n"
"border-radius:4px\n"
"}\n"
"QPushButton:pressed,QCheckBox:pressed,Qmenu:pressed{\n"
"background-color:rgba(0,0,0,0.5);\n"
"color:rgba(255,255,255)\n"
"}\n"
"QPushButton:hover,QCheckBox:hover,Qmenu:hover{\n"
"background-color:rgba(0,0,0,0.3);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.centralwidget.setFont(font)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget.setObjectName("centralwidget")
        self.logLable = QtWidgets.QLabel(self.centralwidget)
        self.logLable.setGeometry(QtCore.QRect(4, 0, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.logLable.setFont(font)
        self.logLable.setStyleSheet("*{color:black;border-radius:10px;font-size:16px}")
        self.logLable.setAlignment(QtCore.Qt.AlignCenter)
        self.logLable.setObjectName("logLable")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(11, 86, 181, 57))
        self.widget_3.setObjectName("widget_3")
        self.autoCountBt = QtWidgets.QPushButton(self.widget_3)
        self.autoCountBt.setGeometry(QtCore.QRect(0, 26, 181, 30))
        self.autoCountBt.setToolTip("")
        self.autoCountBt.setObjectName("autoCountBt")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setGeometry(QtCore.QRect(0, 0, 101, 16))
        self.label.setStyleSheet("*{\n"
"font-size:15px;\n"
"}")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit.setGeometry(QtCore.QRect(140, 0, 41, 20))
        self.lineEdit.setStyleSheet("*{border-image:none;\n"
"background:rgba(255,255,255,0.7);\n"
"border-radius:4px}")
        self.lineEdit.setObjectName("lineEdit")
        self.autoCountBt.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 66, 101, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.togetherBt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.togetherBt.setObjectName("togetherBt")
        self.verticalLayout.addWidget(self.togetherBt)
        self.openDownBt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.openDownBt.setObjectName("openDownBt")
        self.verticalLayout.addWidget(self.openDownBt)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 61, 71))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.setTopBt = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.setTopBt.setStyleSheet("")
        self.setTopBt.setChecked(True)
        self.setTopBt.setTristate(False)
        self.setTopBt.setObjectName("setTopBt")
        self.verticalLayout_2.addWidget(self.setTopBt)
        self.shutdownBt = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.shutdownBt.setObjectName("shutdownBt")
        self.verticalLayout_2.addWidget(self.shutdownBt)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 141, 371, 96))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.autoFriendsBt = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.autoFriendsBt.setToolTip("")
        self.autoFriendsBt.setObjectName("autoFriendsBt")
        self.horizontalLayout_2.addWidget(self.autoFriendsBt)
        self.autoBuildBt = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.autoBuildBt.setObjectName("autoBuildBt")
        self.horizontalLayout_2.addWidget(self.autoBuildBt)
        self.expMapBt = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.expMapBt.setObjectName("expMapBt")
        self.horizontalLayout_2.addWidget(self.expMapBt)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.devConnectBt = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.devConnectBt.setObjectName("devConnectBt")
        self.horizontalLayout.addWidget(self.devConnectBt)
        self.stopAllBt = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.stopAllBt.setObjectName("stopAllBt")
        self.horizontalLayout.addWidget(self.stopAllBt)
        self.startGameBt = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.startGameBt.setObjectName("startGameBt")
        self.horizontalLayout.addWidget(self.startGameBt)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logLable.setText(_translate("MainWindow", "Arknights"))
        self.autoCountBt.setText(_translate("MainWindow", "自动刷本"))
        self.label.setText(_translate("MainWindow", "指定重复次数"))
        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.togetherBt.setText(_translate("MainWindow", "一键三连"))
        self.openDownBt.setText(_translate("MainWindow", "打开掉落图"))
        self.setTopBt.setText(_translate("MainWindow", "置顶"))
        self.shutdownBt.setText(_translate("MainWindow", "关机"))
        self.autoFriendsBt.setText(_translate("MainWindow", "好友访问"))
        self.autoBuildBt.setText(_translate("MainWindow", "基建"))
        self.expMapBt.setText(_translate("MainWindow", "经验五"))
        self.devConnectBt.setText(_translate("MainWindow", "连接设备"))
        self.stopAllBt.setText(_translate("MainWindow", "停止"))
        self.startGameBt.setText(_translate("MainWindow", "启动游戏"))
import ui_rc
