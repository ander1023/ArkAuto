import requests
def getHitokotoText():
    url = 'https://v1.hitokoto.cn/?encode=text'
    str = requests.get(url).text
    # str = '111111111111111111111111111111111111111111'
    lis = list(str)
    outList = [' ',',','.','，','。']
    for i in range(len(lis)):
        if i % 12 == 0:
            for k in range(i-3,i+3):
                if lis[k] in outList:
                    lis.insert(k+1,'\n')
                    break
    s = ''.join(lis)
    # print(s)
    return s
# getHitokotoText()
