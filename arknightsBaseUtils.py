#!/usr/bin/env python
# coding: utf-8
from airtest.aircv import crop_image
from airtest.core.android.android import Android
from airtest.core.api import *
import time
import arknightsData as database
import random

#todo 修改为本地日志
class Utils:
    def __init__(self):
        self.__dev = None


    def connectDev(self):
            try:
                self.__dev = Android('emulator-5554')

            except:
                print('dev not found')
                return False
            if self.__dev != None:
                print('dev connect')
                return True

    # def getdev(self):
    #     return self.__dev
    def startapp(self, name):
        self.__dev.start_app(name, activity=None)

    def sleep(self, second=3):
        time.sleep(second + random.random()*2)

    def touchName(self, name):
        x = database.CM[name][0]
        y = database.CM[name][1]
        self.__dev.touch((x, y), 0.01)
        print('touchList ' + '--' + name + '--')
        self.sleep(3)

    def img_match(self, name):
        try:
            img = database.IM[name][1]
            local_screen = crop_image(self.__dev.snapshot(), (img[0], img[1], img[2], img[3]))
            tempalte = Template(database.IM[name][0])
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
ut = Utils()
