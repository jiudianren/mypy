# _*_ coding: utf-8 _*_

from winpcapy import WinPcapUtils
from winpcapy.winpcapy_types import pcap_file
from winpcapy.winpcapy_types import pcap_open_offline
import winpcapy.winpcapy_types
from winpcapy.winpcapy_types import pcap_pkthdr
from winpcapy.winpcapy_types import pcap_next
from winpcapy.winpcapy_types import c_char_p
from winpcapy.winpcapy_types import pcap_t
from winpcapy.winpcapy_types import pcap_close
from _ctypes import pointer
import logging
from _overlapped import NULL


def pylearnLog(log_level=logging.DEBUG):
    # log实例
    logger = logging.getLogger("GetMacFromPcap")
    # 创建handler 写到控制台，或者日志文件等
    hds = logging.StreamHandler()
    # 给实例增加处理方式
    logger.addHandler(hds)
    # 设置日志级别
    # logger.setLevel(logging.WARN)
    logger.setLevel(log_level)
    return logger


logger = pylearnLog()


# ppkthdr = pointer (pcap_pkthdr()) # 获取指针
# ppkthdr[0] # 指针解引
# 指针判空   bool(ss) 
# filename="F://myworkgit//PyPcap//test.pcap".encode()  # string 转 char *


def print_pcap_pkthdr(pktctx, ppkthdr):
    if isinstance(ppkthdr, pcap_pkthdr):
        info = "caplen={0},len={1},ts:{2}.{3}".format(ppkthdr.caplen, ppkthdr.len, ppkthdr.ts.tv_sec,
                                                      ppkthdr.ts.tv_usec)
        logger.debug(info)

    packetInfo = ""
    for i in range(ppkthdr.len):
        hexs = '{:02x}'.format(pktctx[i])
        packetInfo += hexs
    logger.debug("packetInfo:{0}".format(packetInfo))


'''
数据源：
rulebaseid：取mcs查策略上下文所用的rulebaseid。
RG：取流对应的策略上下文中的RG字段
SI：取流对应的策略上下文中的SI字段，取低三字节

最后一个BYTE的标记：
bit0：是否有enrich策略标记，mcs设置
bit1：enrich成功标记，mcs设置
bit2：1ton标记，dpi设置
bit3：xDPI match标记，dpi设置
bit4：tethering从或欺诈标记，dpi设置
bit5：流送xDPI标记，dpi设置
bit6：是否有redirect标记（不一定是成功），mcs设置
bit7：信令报文标记，mcs设置
'''


def decode_mac(dst, src):
    my_to_hex = lambda x: ('{:02x}'.format(x))
    hexIt = map(my_to_hex, [dst[0], dst[1], dst[2], dst[3]])
    r = list(hexIt)
    print("rulebaseid:{0}{1}{2}{3}".format(r[0], r[1], r[2], r[3]))

    hexIt = map(my_to_hex, [dst[4], dst[5], src[0], src[1]])
    r = list(hexIt)
    print("RG:{0}{1}{2}{3}".format(r[0], r[1], r[2], r[3]))

    hexIt = map(my_to_hex, [src[2], src[3], src[4]])
    r = list(hexIt)
    print("SI:{0}{1}{2}".format(r[0], r[1], r[2]))
    print("FLAGS:{0}".format(my_to_hex(src[5])))
    bitFlag = src[5]
    print("enrich flag    :{0}".format(bitFlag & 0x01 == True))
    print("enrich success :{0}".format(bitFlag & 0x02 == True))
    print("1ton           :{0}".format(bitFlag & 0x04 == True))
    print("xDPI Mathch    :{0}".format(bitFlag & 0x08 == True))
    print("tethering从或欺诈  :{0}".format(bitFlag & 0x10 == True))
    print("流送xDPI        :{0}".format(bitFlag & 0x20 == True))
    print("redirect标记              :{0}".format(bitFlag & 0x40 == True))
    print("信令报文标记                      :{0}".format(bitFlag & 0x70 == True))


def get_mac_info(pktctx):
    # print(type(pktctx))
    if isinstance(pktctx[0], int) == False:
        logger.error("type erro!")
        return

    src = pktctx[0:6]
    dst = pktctx[6:12]

    # 使用lambda 表达式
    tempSrc = ""
    for i in src:
        hexs = '{:02x}'.format(i)
        tempSrc += hexs;
    print("src:{0}".format(tempSrc))

    tempSrc = ""
    for i in dst:
        hexs = '{:02x}'.format(i)
        tempSrc += hexs;
    print("dst:{0}".format(tempSrc))
    decode_mac(dst, src)


def ReadPacp(mypcap_t):
    if isinstance(mypcap_t[0], pcap_t) == False:
        # todo how to make sure the  mypcap_t's type is what
        logger.debug(type(mypcap_t))
        # logger.debug( type(pcap_t))

    ppkthdr = pointer(pcap_pkthdr())  # 获取指针
    pkt = pcap_next(mypcap_t, ppkthdr)
    pktCnt = 1

    while bool(pkt):
        print("pack cnt:{0}".format(pktCnt))
        if logger.level == logging.DEBUG:
            print_pcap_pkthdr(pkt, ppkthdr[0])

        if ppkthdr[0].len < 12:
            logger.error("erro packt or cann't judge this packer")
        else:
            get_mac_info(pkt)

        pkt = pcap_next(mypcap_t, ppkthdr)
        pktCnt += 1
        print("\n")

    logger.debug(" Total {0} packet in this file".format(pktCnt))
    logger.error("End Process sucessfully.(｡◕ˇ∀ˇ◕)")


def open_pcap_file(filename):
    if isinstance(filename, str) == False:
        logger.error("your input is not a str, exit now!!!!")
        logger.error("****---exit now---***")
        return

    errobuf = c_char_p()
    fncode = filename.encode()  # string 转 char *
    mypcap_t = pcap_open_offline(fncode, errobuf)
    if bool(mypcap_t) == False:
        logger.error("{0} may be not a file or a pcap file!".fomat(filename))
        logger.error(errobuf)
        logger.error("****---exit now---***")
        pcap_close(mypcap_t)
    else:
        ReadPacp(mypcap_t)
        pcap_close(mypcap_t)


def get_input_filename():
    prompt = '''please input your pcap file path or quit:
    Example : 1,path : F://myworkgit//PyPcap//test.pcap
              2,quit : quit
    '''
    file_name = input(prompt)
    print("please comfirm your input:{0}".format(file_name))
    return file_name


if __name__ == "__main__":
    logger.setLevel(logging.ERROR)
    logger.debug("ahha")
    # filename="F://myworkgit//PyPcap//test.pcap"
    filename = get_input_filename()
    while filename != "quit":
        print("ahha ")
        open_pcap_file(filename)
        filename = get_input_filename()

    print("Bye Bye")

# help(pcap_file)
# help(WinPcapUtils)
