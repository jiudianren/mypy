# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/7/26 9:28

# !/usr/bin/python3
# -*- coding: utf-8 -*-

from socket import *
import os
import logging
import functools
import  os
from tkinter import *
from tkinter.filedialog import askdirectory ,askopenfilename
import  threading
import _thread
import datetime


# 配置开始
interval_ms = 500  # 单位毫秒  socket 链接超时时间
repeate_time = 10000 # tcp 建链 次数  10
ip_and_port_list = [
    {'ip': '58.60.230.115', 'port': 443}, {'ip': '210.21.223.9', 'port': 443},
    {'ip': '222.88.95.249', 'port': 80}, {'ip': '111.13.141.205', 'port': 80},
    {'ip': '111.13.141.239', 'port': 443}, {'ip': '106.11.248.98', 'port': 80},
    {'ip': '117.185.17.176', 'port': 443}, {'ip': '183.232.91.123', 'port': 8011},
    {'ip': '106.11.250.202', 'port': 80}, {'ip': '203.119.205.113', 'port': 80},
    {'ip': '120.55.23.45', 'port': 443}, {'ip': '121.43.19.249', 'port': 443},
    {'ip': '203.119.207.252', 'port': 443}, {'ip': '117.187.206.110', 'port': 443},
    {'ip': '117.187.206.59', 'port': 80}, {'ip': '117.135.252.140', 'port': 80},
    {'ip': '39.130.161.45', 'port': 443}, {'ip': '161.117.71.226', 'port': 443}
]
# 配置结束
date_lock = threading.Lock()


def pylearnLog(log_level=logging.DEBUG ):
    # log实例
    logger = logging.getLogger("GetMacFromPcap")
    # 创建handler 写到控制台，或者日志文件等
    hds = logging.StreamHandler()
    #fds = logging.FileHandler("C://Users//10259187//Desktop//Test//log.txt",mode='w', encoding='utf-8')
    # 给实例增加处理方式
    logger.addHandler(hds)
    # 设置日志级别
    # logger.setLevel(logging.WARN)
    logger.setLevel(log_level)
    return logger

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


def check_new_file(file_name,tip = "选取结果文件将存放的目录"):
    tips = "选取结果文件将存放的目录"
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

logger = pylearnLog()
logger.setLevel(logging.DEBUG)
out_data = dict()  # ip_port:connet_data
def insert_out_data(ip, port, con_result ):
    global out_data
    if (ip, port) in out_data.keys():
        date_lock.acquire()
        pre_value = out_data[(ip, port)]
        if con_result:
            pre_value["Sucess"] += 1;
        else:
            pre_value["Fail"] += 1;
        date_lock.release()
    else:
        new_value = dict()
        new_value["Sucess"] = 0;
        new_value["Fail"] = 0;
        if con_result:
            new_value["Sucess"]  = 1;
        else:
            new_value["Fail"]  = 1 ;
        date_lock.acquire()
        out_data[(ip, port)] = new_value
        date_lock.release()


def portScanner(host, port):
    con_result = False
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((host, port))
        con_result = True
        #logger.debug('[+] %s %d open' % (host, port))
    except:
        con_result = False
        #logger.debug('[-] %s %d close' % (host, port))
    finally:
        s.close()
        insert_out_data(host, port,con_result)


def thread_func( thread_seq, ipandport):
    logger.debug("start therad {0}".format(thread_seq))
    host = ipandport['ip']
    port = ipandport['port']
    con_result = False
    global  repeate_time
    for p in range(0, repeate_time):
        try:
            s = socket(AF_INET, SOCK_STREAM)
            s.connect((host, port))
            con_result = True
            #logger.debug('[+] %s %d open' % (host, port))
        except:
            con_result = False
            #logger.debug('[-] %s %d close' % (host, port))
        finally:
            s.close()
            insert_out_data(host, port,con_result)
    logger.debug("end therad {0}".format(thread_seq))

def show_result():
    global out_data
    for (k,v) in  out_data.items():
        #print( k,v)
        total = v['Sucess'] + v['Fail']
        fail_rat = v['Fail']/total
        kl =list(k)
        print( "connect ip:{0},Fail rate:{1},sucess time:{2},fail time:{3}".format(k,fail_rat, v['Sucess'],v['Fail']))

def out_put_data(file_name):
    global out_data
    try:
        fd = open(file_name, "w", newline='\r\n')
        lines = []
        all_total = 0
        all_fail = 0
        all_sucess = 0

        for (k, v) in out_data.items():
            # print( k,v)
            total = v['Sucess'] + v['Fail']
            all_total += total
            all_fail +=  v['Fail']
            all_sucess += v['Sucess']
            fail_rat = v['Fail'] / total

            lines.append("connect ip:{0},Fail rate:{1},sucess time:{2},fail time:{3} \n".format(k,
                                                                                             fail_rat, v['Sucess'],  v['Fail']))
        total_fail_rat  = all_fail/all_total
        lines.append("==============Total Info: ============\n")
        total_str = "Total Fail Rate :{0},Total Packt:{1}, Total Fail Packt: {2},Total Sucess Packt: {3} \n".format(total_fail_rat,
                                all_total, all_fail, all_sucess)
        lines.append(total_str)
        print(total_str)
        fd.writelines(lines)
    except Exception as e:
        print('please check your file formate :', e, )
        print('file', e.__traceback__.tb_frame.f_globals['__file__'])
        print('num', e.__traceback__.tb_lineno)
    finally:
        fd.close()



def main():
    start = datetime.datetime.now()
    out_data.clear()
    file_name = check_new_file(file_name="result.txt")
    print("save out result file {0}".format(file_name))
    print("time out:{0}ms".format(interval_ms))
    print("repeat time :{0}".format(repeate_time))
    time_out = interval_ms/1000
    logger.debug("time out :{0}s".format(time_out))
    setdefaulttimeout(time_out)

    thread_list = []
    i = 0
    for ipandport in ip_and_port_list:
        i += 1
        t = threading.Thread(target=thread_func , args = (i,ipandport ))
        thread_list.append(t)

    for t in thread_list:
        t.setDaemon(True)
        t.start()

    for t in thread_list:
        t.join()

    #show_result()
    out_put_data(file_name)
    end = datetime.datetime.now()
    print("start_time:{0},end_time:{1}, used: {2}".format(start,end, end - start))

if __name__ == '__main__':
    main()
