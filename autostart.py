# -*- coding: UTF-8 -*-

import io
import json
import time

from pywinauto import application
import win32api,win32con

#路径需要使用双斜线
#{
#"local":["C:\\Users\\10259187\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe","F:\\Program Files\\ListaryProv\\Listary Pro v5.00.2843\\Listary Pro\\Listary.exe" ]
#}

chrome=r"C:\Users\10259187\AppData\Local\Google\Chrome\Application\chrome.exe"
#app = application.Application().start(chrome)
print(chrome.__len__())


def readapps(startfile):
    apps =[]
    with open(startfile,'r') as load_f:
        print(startfile)
        loadItem = json.load(load_f)
        for it in loadItem["local"] :
            print(it)
            apps.append(it)
    return apps        


def startpro(apps):
    for it in apps:
        tips=r"start up:"
        tips += it
        win32api.MessageBox(0, tips, "提示")
        print (it)
        app2 = application.Application().start(it)
        time.sleep(10)


startfile="F:\jiudianren\startup.json"
win32api.MessageBox(0, "即将开始启动程序", "提示")   
apps = readapps(startfile) 
startpro(apps)
    
