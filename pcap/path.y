# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/7/3 16:51

# https://blog.csdn.net/zjiang1994/article/details/53513377/
from tkinter import *
from tkinter.filedialog import askdirectory ,askopenfilename
import functools


def msg_on_click(root):
    root.quit()
    root.destroy()

def msg_box( msg_str:str):
    mypath=[""]
    root = Tk()
    Label(root, text=msg_str).grid(row=0, column=0)
    Button(root, text="点击确认", command=functools.partial(msg_on_click,root )).grid(row=1, column=0)
    root.mainloop()
    return mypath[0]


def on_click(root,path):
    aa = path.get()
    if len(aa) == 0:
        msg_box("no path or file be selected,and exit now .......")
        exit()
    root.quit()
    root.destroy()


def selectPath(var, path):
    path_ = askdirectory()
    var[0] = path_
    print(var[0])
    path.set(path_)


def selectFile(var, path):
    path_ = askopenfilename()
    var[0] = path_
    path.set(path_)

# 获取一个文件夹路径 "选取PCAP文件所在文件夹:"
def get_os_path(tip_str):
    mypath=[""]
    root = Tk()
    path = StringVar()
    Label(root, text=tip_str).grid(row=0, column=0)
    Entry(root, textvariable=path).grid(row=0, column=1)
    Button(root, text="路径选择", command=functools.partial(selectPath,mypath, path )).grid(row=0, column=2)
    Button(root, text="点击确认", command=functools.partial(on_click,root, path )).grid(row=1, column=0)
    root.mainloop()
    return mypath[0]

# 获取一个文件路径
def get_os_file_path():
    mypath=[""]
    root = Tk()
    file_name_str = StringVar()
    Label(root, text="选取 ServiceIp.json:").grid(row=0, column=0)
    Entry(root, textvariable=file_name_str).grid(row=0, column=1)
    Button(root, text="文件选择", command=functools.partial(selectFile,mypath, file_name_str )).grid(row=0, column=2)
    Button(root, text="点击确认", command=functools.partial(on_click,root, file_name_str )).grid(row=1, column=0)
    root.mainloop()
    return mypath[0]

#print(get_os_path("tip"))
#print(get_os_file_path())
