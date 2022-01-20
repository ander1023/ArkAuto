import os
print('-- 请输入分钟数 --')
print('-- 输入0时为立即关机 --')
print('-- 输入-1时为取消关机 --')
time = input()
order = 'shutdown /s /f /t ' + str(60*int(time))
if int(time) == 0 :
    os.system('shutdown /s /t 0')
elif int(time )==-1:
    os.system('shutdown /a')
else:
    os.system(order)

