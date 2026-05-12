import numpy as np
import pyautogui as pag
import time
time.sleep(4)
xy=[[1187,871],[1304,864],[1429,859],[1578,869],[1712,865],[1717,995],[1584,986],[1445,973],[1268,982],[1195,988],[1179,1114],[1309,1119],[1442,1127],[1577,1142],[1695,1149],[1704,1247],[1587,1258],[1424,1264],[1320,1264],[1320,1264],[1165,1258],[1167,1368],[1308,1388],[1432,1397],[1567,1418],[1716,1403]]
print(xy[0])
for i in range(100):
    time.sleep(np.random.rand()*2)
    pag.moveTo(1540, 1585)
    pag.click()
    check=[]
    for j in range(3):
       r= np.random.randint(0,25)
       time.sleep(np.random.rand())
       while r in check:
           r = np.random.randint(0, 25)
       check.append(r)
       time.sleep(np.random.rand())
       pag.moveTo(xy[r][0],xy[r][1])
       pag.click()
    time.sleep(np.random.rand()*1)
    pag.moveTo(1540, 1585)
    pag.click()
    time.sleep(np.random.rand()*2)


