# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/7/3 16:51

# https://blog.csdn.net/zjiang1994/article/details/53513377/
import functools
import  os
from tkinter import *
from tkinter.filedialog import askdirectory ,askopenfilename

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
    Label(root, text="选取文件:").grid(row=0, column=0)
    Entry(root, textvariable=file_name_str).grid(row=0, column=1)
    Button(root, text="文件选择", command=functools.partial(selectFile,mypath, file_name_str )).grid(row=0, column=2)
    Button(root, text="点击确认", command=functools.partial(on_click,root, file_name_str )).grid(row=1, column=0)
    root.mainloop()
    return mypath[0]


def check_new_file(tip,file_name):
    tips = "选取新建文件将存放的目录"
    if len(tip)  > 0:
        tips = tip
    dir = get_os_path(tips)

    new_file="py_comm_new_file.txt"
    if len(file_name)  > 0:
        new_file = file_name
    index = 0
    while os.access(os.path.join( dir, file_name), os.R_OK) == True:
        index += 1
        name = file_name.split(".")
        inner = name[0].split("_")
        if len(inner) ==1:
            name[0] =  inner[0]+"_"+str(index)
        elif  inner[-1].isdigit():
            inner[-1] = str(index)
            name[0] = "_".join( inner, )
        else:
            name[0] +"_"+str(index)

        file_name = (name[0] + "." + name[1])
    file_name = os.path.join(dir, file_name)
    return file_name


def get_dir_files(file_path):
    """
    :param file_path: 文件夹路径
    :return: 文件夹下的所有文件
    """
    file_list = []
    if not os.access(file_path,os.R_OK) :
        print("NO pcap FILE PATH IN {0}".format(file_path))
        return file_list
    for file_name in os.listdir(file_path):
        file_name = os.path.join(file_path, file_name)
        file_list.append(file_name)
    return file_list


def get_new_file_full_path(file_name):
    """
    :param file_name: 文件名
    :return: 文件的全路径
    如果有重复文件，则会在文件后加序号以区分，序号递增
    """
    aim_dir = get_os_path("选取结果文件将存放的目录")
    file_name = os.path.join(aim_dir, file_name)
    index = 0
    while os.access(os.path.join(aim_dir, file_name), os.R_OK) == True:
        index += 1
        name = file_name.split(".")
        inner = name[0].split("_")
        name[0] = inner[0]+"_"+inner[1] + "_"+str(index)
        file_name = (name[0] + "." + name[1])

    file_name = os.path.join(aim_dir, file_name)
    return file_name

#print(get_os_path("tip"))
#print(get_os_file_path())
