# -*- coding: UTF-8 -*-

import io
from pywinauto import application
import time
import win32api,win32con


im=r"C:\Program Files (x86)\ZTE\ZTE IM9\IM9.exe"
chrome=r"C:\Users\10259187\AppData\Local\Google\Chrome\Application\chrome.exe"
listray="F:\Program Files\ListaryProv\Listary Pro v5.00.2843\Listary Pro\Listary.exe"
cmd=r"C:\Windows\System32"
eclipse="F:\eclipse\eclipse.exe"
pyeclipse="F:\pyeclipse\pyeclipse.exe"

app = application.Application().start(chrome)
def readapps(startfile):
    fp = open(startfile, 'r')
    apps=[]
    while True :
        item =  fp.readline()    
        if item :
            apps.append(item)
        else :
            break
    return apps        


def startpro(apps):
    for it in apps:
        
        tips=r"start up:"
        tips += it
        win32api.MessageBox(0, tips, "提示")
        print (it)
        app2 = application.Application().start(it)
        time.sleep(10)

win32api.MessageBox(0, "即将开始启动程序", "提示")


startfile="F:\jiudianren\startup.txt"   
apps = readapps(startfile) 
startpro(apps)
    
