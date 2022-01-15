import os
os.system('pyuic5 -o arknightsUI.py arknightsUI.ui')
print('已转换ui文件')
os.system(' pyrcc5 ui.qrc -o ui_rc.py ')
print('已转换qrc文件')
