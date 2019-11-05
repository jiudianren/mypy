# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/7/3 16:51

# https://blog.csdn.net/zjiang1994/article/details/53513377/
import functools
import os
from tkinter import *
from tkinter.filedialog import askdirectory, askopenfilename


def msg_on_click(root):
    root.quit()
    root.destroy()


def msg_box(msg_str: str):
    root = Tk()
    Label(root, text=msg_str).grid(row=0, column=0)
    Button(root, text="点击确认", command=functools.partial(msg_on_click, root)).grid(row=1, column=0)
    root.mainloop()
    return


def on_click(root, path):
    aa = path.get()
    if len(aa) == 0:
        msg_box("no path or file be selected,and exit now .......")
        exit()
    root.quit()
    root.destroy()


def select_path(var, path, use_type):
    if use_type == 1:
        var[0] = askopenfilename()
    else:
        var[0] = askdirectory()
    path.set(var[0])


def get_path(use_type, used_tip, confirm_tip="点击确认"):
    '''

    :param use_type: 1:选择文件 2：选择文件夹
    :param used_tip: 使用它提示
    :param confirm_tip: 确认提示
    :return: 返回选择文件或者文件夹的路径
    '''
    return_path = [""]
    root = Tk()
    file_name_str = StringVar()

    if len(used_tip) == 0:
        used_tip = "用途提示："

    ust_type_str = ""
    if use_type == 1:
        ust_type_str = "文件选择"
    else:
        ust_type_str = "路径选择"

    Label(root, text=used_tip).grid(row=0, column=0)
    Entry(root, textvariable=file_name_str).grid(row=0, column=1)
    Button(root, text=ust_type_str,
           command=functools.partial(select_path, return_path, file_name_str,use_type)).grid(row=0, column=2)
    Button(root, text=confirm_tip, command=functools.partial(on_click, root, file_name_str)).grid(row=1, column=0)
    root.mainloop()
    return return_path[0]


def check_new_file(tip, file_name):
    tips = "选取新建文件将存放的目录"
    if len(tip) > 0:
        tips = tip
    dir = get_path(2, tips)

    new_file = "py_comm_new_file.txt"
    if len(file_name) > 0:
        new_file = file_name
    index = 0
    while os.access(os.path.join(dir, file_name), os.R_OK) == True:
        index += 1
        name = file_name.split(".")
        inner = name[0].split("_")
        if len(inner) == 1:
            name[0] = inner[0] + "_" + str(index)
        elif inner[-1].isdigit():
            inner[-1] = str(index)
            name[0] = "_".join(inner, )
        else:
            name[0] + "_" + str(index)

        file_name = (name[0] + "." + name[1])
    file_name = os.path.join(dir, file_name)
    return file_name


def get_dir_files(file_path):
    """
    :param file_path: 文件夹路径
    :return: 文件夹下的所有文件
    """
    file_list = []
    if not os.access(file_path, os.R_OK):
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
    aim_dir = get_path(2, "选取结果文件将存放的目录")
    file_name = os.path.join(aim_dir, file_name)
    index = 0
    while os.access(os.path.join(aim_dir, file_name), os.R_OK):
        index += 1
        name = file_name.split(".")
        inner = name[0].split("_")
        name[0] = inner[0] + "_" + inner[1] + "_" + str(index)
        file_name = (name[0] + "." + name[1])

    file_name = os.path.join(aim_dir, file_name)
    return file_name


if __name__ == '__main__':
    print(get_path(1, "测试文件"))
    print(get_path(2, "测试文件夹", "敢不敢确认"))
    print("Test 获取文件夹下的所有文件")
    print(get_dir_files())
    print("在文件夹下 新建 文件")
    print(get_new_file_full_path("测试文件名.txt"))
