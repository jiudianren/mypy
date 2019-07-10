# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/6/28 10:51

import os
import csv
import logging
import sys
import binascii
import socket
from binascii import hexlify
import scapy.all as scapy

from MyCommon import get_input_filename
from MyCommon import get_pcap_files
from MyCommon import get_dir_files
from MyCommon import pylearnLog
from FiveTuple import FiveTuple
from csv_deal import csv_value
from csv_deal import out_put_file
from Server import read_server_ip_from_file
from MyCommon import logger
from path import get_os_path, get_os_file_path,msg_box

lpf_debug_flag = False
# ip 使用字符串的形式
serv_ip_pool = set()
ue_ip_poll = set()

# out_data  (key:value )
# key --> tuple( FiveTupe, rulebaseid)
# value -->map（key: value）
out_data = dict()


def show_csv():
    global out_data
    index = 0
    for (k, v) in out_data.items():
        logger.debug("---------------------------")
        logger.debug("index:{0}".format(index))
        logger.debug("key:{0}_{1}".format(k[0], k[1]))
        logger.debug("value:{0}".format(v))
        index += 1
    out_put_file(out_data)

def get_serv_ip():
    #file_name = os.path.join(sys.path[0], "ServiceIp.json")
    file_name = get_os_file_path()
    #msg_box("ServiceIp 取自文件"+file_name)
    global serv_ip_pool
    re = read_server_ip_from_file(file_name)
    if not re[0]:
        print("sorry ,there are some question with the json file .it is goningto exit this  program .")
        exit(0)
    else:
        serv_ip_pool = re[1]
        logger.debug( "server ip pool:{0}".format(serv_ip_pool))
    return serv_ip_pool


def insert_ue_ip(ip):
    logger.debug("insert_ue_ip:{0}".format(ip))
    global ue_ip_poll
    ue_ip_poll.add(ip)


def is_gtp(pkt):
    """
        UDP && src.port==2152 && dest.port==2152
    """
    if (pkt.payload.proto == 17) and (pkt.payload.payload.sport == 2152) and (pkt.payload.payload.dport == 2152):
        # 17 is UDP
        logger.debug("GTP")
        return True
    return False


def insert_out_data(key1, key2, value):
    global out_data
    if (key1, key2) in out_data.keys():
        logger.debug("update value")
        last_value = out_data[(key1, key2)]
        last_value[csv_value.DwDirVol] += value[csv_value.DwDirVol]
        last_value[csv_value.UpDirVol] += value[csv_value.UpDirVol]

        # 如果有不一样的地方，做出打印警告
        if (last_value[csv_value.UpDirRG] != value[csv_value.UpDirRG]) or \
                (last_value[csv_value.DwDirRG] != value[csv_value.DwDirRG]) or \
                (last_value[csv_value.UpDirSI] != value[csv_value.UpDirSI]) or \
                (last_value[csv_value.DwDirSI] != value[csv_value.DwDirSI]) or \
                (last_value[csv_value.Flags] != value[csv_value.Flags]):

            logger.debug("pre info: {0},{1},{2},{3},{4}".format(last_value[csv_value.UpDirRG],
                                                                last_value[csv_value.DwDirRG],
                                                                last_value[csv_value.UpDirSI],
                                                                last_value[csv_value.DwDirSI],
                                                                last_value[csv_value.Flags]))
            logger.debug("cur info: {0},{1},{2},{3},{4}".format( value[csv_value.UpDirRG],
                                                                 value[csv_value.DwDirRG],
                                                                 value[csv_value.UpDirSI],
                                                                 value[csv_value.DwDirSI],
                                                                 value[csv_value.Flags] ))

            print(" this set is not same in RG or Si or Flags")
        out_data[(key1, key2)] = last_value
    else:
        logger.debug("insert value {0}-{1}___{2}".format(key1, key2, value))
        out_data[(key1, key2)] = value


def get_part_csv_value(mac, up_send_flag=True):
    dst_hex = mac['dst'].replace(':', '')
    src_hex = mac['src'].replace(':', '')

    temp_rg = dst_hex[8:12] + src_hex[0:4]
    logger.debug("temp_rg {0}".format(temp_rg))
    if up_send_flag:
        up_dir_rg = socket.ntohl(int(temp_rg, 16))
        dw_dir_rg = "null"

        up_dir_si = socket.ntohl(int(dst_hex[4:10], 16))
        dw_dir_si = "null"
    else:
        up_dir_rg = "null"
        dw_dir_rg = socket.ntohl(int(temp_rg, 16))

        up_dir_si = "null"
        dw_dir_si = socket.ntohl(int(dst_hex[4:10], 16))

    bit_flags = int(src_hex[10:12], 16)
    if True:
        logger.debug("UpdirSI :{0}".format(up_dir_si))
        logger.debug("DwDirSi :{0}".format(dw_dir_si))
        logger.debug("UpDirRG :{0}".format(up_dir_rg))
        logger.debug("DwDirRG :{0}".format(dw_dir_rg))
        logger.debug("BitFlags :{0}".format(bit_flags))

    cvs = {csv_value.UpDirRG: up_dir_rg,
           csv_value.DwDirRG: dw_dir_rg,
           csv_value.UpDirSI: up_dir_si,
           csv_value.DwDirSI: dw_dir_si,
           csv_value.Flags: bit_flags,
           csv_value.F_enrich: 1 if (bit_flags & 0x01) else 0,
           csv_value.F_enrich_sucess: 1 if (bit_flags & 0x02) else 0,
           csv_value.F_1ton: 1 if (bit_flags & 0x04) else 0,
           csv_value.F_xDpi_match: 1 if (bit_flags & 0x08) else 0,
           csv_value.F_tethering: 1 if (bit_flags & 0x10) else 0,
           csv_value.F_flow_xDPI: 1 if (bit_flags & 0x20) else 0,
           csv_value.F_redirect: 1 if (bit_flags & 0x40) else 0,
           csv_value.F_signal_msg: 1 if (bit_flags & 0x80) else 0 }
    return cvs


def deal_dl_send(us_pkt, mac):
    logger.debug("deal_dl_send")
    # logger.debug(us_pkt.payload.show)
    logger.debug(mac)

    firstKey = FiveTuple(us_pkt.payload.src, us_pkt.payload.payload.sport, \
                         us_pkt.payload.dst, us_pkt.payload.payload.dport, us_pkt.payload.proto)

    #   SRC DST都是 str类型 需要转化一下
    if False:
        temp = bytearray.fromhex(mac['src'].replace(':', ''))
        src_list = list(temp)
        logger.debug(src_list)

    dst_hex = mac['dst'].replace(':', '')
    rule_base_id = socket.ntohl(int(dst_hex[0:8], 16))
    cvs = get_part_csv_value(mac, False)
    cvs[csv_value.DwDirVol] = us_pkt.payload.len
    cvs[csv_value.UpDirVol] = 0
    logger.debug("cvs:{0}".format(cvs))
    insert_out_data(firstKey, rule_base_id, cvs)


def decode_gtp(gtp):
    # 当做大端来处理
    gtp_head_len = 8
    flags = gtp[0]
    msg_type = gtp[1]
    length = gtp[2:4]
    teid = gtp[4:8]
    if False:
        logger.debug('flags:{:02x},msg_type:{:02x}'.format(flags, msg_type))
        logger.debug('length:{0}'.format(binascii.b2a_hex(length)))
        logger.debug('teid:{0}'.format(binascii.b2a_hex(teid)))

    if flags & 0x07:
        # Optional Field
        #logger.debug('Optional Field:{0}'.format(binascii.b2a_hex(gtp[8:12])))
        gtp_head_len += 4
    user_pck = gtp[gtp_head_len:]
    logger.debug("user pkt:{0}".format(binascii.b2a_hex(user_pck)))
    return user_pck


def add_ether(btarr, ip_v6_flag=False):
    # 默认IPV4
    if ip_v6_flag:
        btarr.insert(0, 0xdd)
        btarr.insert(0, 0x86)
    else:
        btarr.insert(0, 0x00)
        btarr.insert(0, 0x08)

    for i in range(12):
        btarr.insert(0, 0x00)
    return btarr


# gtp解码 参考 psVpfuMcsGTPV1HeadDecap
def get_ue_pkt(gtp_pkt):
    logger.debug("gtp_pkt_len:{0}".format(len(gtp_pkt['Raw'].load)))
    gtp = gtp_pkt['Raw'].load
    # logger.debug("hex gtp:{0}".format(binascii.b2a_hex(gtp)))
    us_pkt = decode_gtp(gtp)

    # 判断是 ip_v4 or ip_v6
    # logger.debug("IP_VERSION Flag:{0}".format(us_pkt[0]))
    btarr = 0X00
    if us_pkt[0] == 0X45:
        btarr = add_ether(bytearray(us_pkt))
    else:
        btarr = add_ether(bytearray(us_pkt), True)

    us_pkt = scapy.Ether(btarr)
    return us_pkt


def deal_gtp_pck(gtp_pkt, index):
    mac = {'src': gtp_pkt.src, 'dst': gtp_pkt.dst}
    us_pkt = get_ue_pkt(gtp_pkt)
    logger.debug("deal_gtp_pck :{0}".format(mac))

    if gtp_pkt.payload.dst in serv_ip_pool:
        insert_ue_ip(us_pkt.payload.src)
    elif gtp_pkt.payload.src in serv_ip_pool:
        deal_dl_send(us_pkt, mac)
    else:
        logger.debug("pass the {0} packet".format(index))

def deal_up_send(pkt, mac):
    logger.debug("deal up send")
    firstKey = FiveTuple(pkt.payload.dst, pkt.payload.payload.dport, \
                         pkt.payload.src, pkt.payload.payload.sport, pkt.payload.proto)

    logger.debug(firstKey)
    dst_hex = mac['dst'].replace(':', '')
    rule_base_id = socket.ntohl(int(dst_hex[0:8], 16))
    # logger.debug("n:{0} h:{1}".format(rulebase_id,socket.ntohl(rulebase_id)))

    cvs = get_part_csv_value(mac)
    cvs[csv_value.DwDirVol] = 0
    cvs[csv_value.UpDirVol] = pkt.payload.len
    insert_out_data(firstKey, rule_base_id, cvs)


def deal_us_pkt(pkt, index):
    logger.debug("deal_us_pkt dst:{0},src:{1}".format(pkt.dst, pkt.src))
    mac = {'src': pkt.src, 'dst': pkt.dst}
    logger.debug("src:{0}".format(pkt.payload.src))
    if pkt.payload.src in ue_ip_poll:
        deal_up_send(pkt, mac)
    else:
        logger.debug("pass the {0} packet".format(index))


def read_pcap(file_list):
    for it in  file_list:
        index = 1
        try:
            pkts = scapy.rdpcap(it)
            pkts_cn = len(pkts)
            if pkts_cn <= 0:
                logger.error("No packet in this file ,please check your file !!")
                return
            else:
                logger.debug("Total Packet Cnt:{0}".format(pkts_cn))
            for pkt in pkts:
                logger.debug("Packt Index {0}".format(index))
                if is_gtp(pkt):
                    deal_gtp_pck(pkt, index)
                else:
                    deal_us_pkt(pkt, index)
                index += 1
                logger.debug("\n \n")
        except Exception as e:
            logger.debug("Erro Reasion:{0},{1},{2}".format(e, index,it))
            print("Erro Reasion: ",e)
            print("Pass this file {0}".format(it))


if __name__ == "__main__":
    if "lpf_debug_flag" in sys.argv:
        logger.setLevel(logging.DEBUG)
        lpf_debug_flag = True
    else:
        logger.setLevel(logging.WARNING)
    get_serv_ip()
    pcap_dir = get_os_path("选取PCAP文件所在文件夹:")
    file_list = get_dir_files(pcap_dir)
    read_pcap(file_list)
    show_csv()
    print("Bye Bye")
