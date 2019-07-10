# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/6/28 10:52

import logging
import os
from path import get_os_path, get_os_file_path,msg_box

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

logger = pylearnLog()

def get_input_filename(file_type=1):
    prompt = ''
    if file_type == 2:
        prompt = '''please input your service_ip json  file path :
                Example: F:/myworkgit/PyPcap/test.pcap
                '''
    else:
        prompt = '''please input your pcap file path or quit:
                Example : 1,path : F:/myworkgit/PyPcap/pcap/3/t.pcap
                          2,quit : quit
                
                please input your file path, here:
                '''

    file_name = input(prompt)
    print("please comfirm your input:{0}".format(file_name))
    return file_name

def get_pcap_files(tip_dir):
    file_list = []
    pcap_dir = os.path.join(tip_dir, "pcap")
    msg_box("PCAP 取自文件:"+pcap_dir)
    logger.debug("dir{0}  {1}".format(tip_dir,pcap_dir))
    if not os.access(pcap_dir,os.R_OK) :
        print("NO pcap FILE PATH IN {0}".format(tip_dir))
        return file_list
    for file_name in os.listdir(pcap_dir):
        file_name = os.path.join(pcap_dir, file_name)
        file_list.append(file_name)
    return  file_list

def get_dir_files(dir):
    file_list = []
    if not os.access(dir,os.R_OK) :
        print("NO pcap FILE PATH IN {0}".format(dir))
        return file_list
    for file_name in os.listdir(dir):
        file_name = os.path.join(dir, file_name)
        file_list.append(file_name)
    return  file_list

