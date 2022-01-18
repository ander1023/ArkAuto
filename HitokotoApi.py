#!/usr/bin/env python
# coding: utf-8
import requests


def getHitokotoText():
    url = 'https://v1.hitokoto.cn/?c=a&c=b&c=c&encode=text'
    #接口https://hitokoto.cn/
    str = requests.get(url).text
    lis = list(str)
    outList = [' ','。',',','.','，',]
    for i in range(1,len(lis)):
        if i % 12 == 0:
            for k in range(i-3,i+3):
                if lis[k] in outList:
                    lis.insert(k+1,'\n')
                    break
    s = ''.join(lis)
    # print(s)
    return s
# getHitokotoText()
