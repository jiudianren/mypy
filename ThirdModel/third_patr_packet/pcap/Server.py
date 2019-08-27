# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/7/1 15:30

import os
import json
import re

# get server ip from file

def judge_legal_ip_v4(str):
    '''
    正则匹配方法
    判断一个字符串是否是合法IP地址
    '''
    compile_ip = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if compile_ip.match(str):
        return True
    else:
        return False


def read_server_ip_from_file(filename):
    deal_flage: bool = False
    ip_json = ''
    if os.access(filename, os.R_OK) == False:
        print('please check your file is exit or not.')
        deal_flage = False
    else:
        try:
            fhd = open(filename)
            total_json = json.load(fhd)
            deal_flage = True
            ip_json = total_json["IP"]
            for item in ip_json:
                if not judge_legal_ip_v4(item):
                    #ip_json.remove(item)
                    print("this IP:[{0}] is illegal IP V4.".format(item))

            if total_json["num"] != len(ip_json):
                print('Warning: your ip num is {0},but available IP is {1}'.format(total_json["num"], str(len(ip_json))))
            else:
                pass
        except Exception as e:
            print('please check your json formate :', e)
        finally:
            fhd.close()
    return (deal_flage, ip_json)


# 检查文件是否存在
# json读文件
# 获取ip
# return tuple(True/False, IPList)


if __name__ == "__main__":
    print("Test File: F:/myworkgit/PyPcap/lpf/3/t.pcap")
    # filename = get_input_filename()
    filename = "F:/myworkgit/PyPcap/ServiceIp.json"
    re = read_server_ip_from_file(filename)
    if not re[0]:
        print("file erro .no json ")
    else:
        print("json:{}".format(re[1]))
    print("Bye Bye")
