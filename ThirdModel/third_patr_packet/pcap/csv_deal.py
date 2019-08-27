# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/7/1 9:39

from enum import Enum, unique
from MyCommon import pylearnLog
import os,sys,csv, time
from FiveTuple import FiveTuple
#  UpDirRG + DwDirRG + 位标记   UpdirVol DwDirVol  UpdirSI DwDirSi
from path import  msg_box
from MyCommon import logger
from path import get_os_path, get_os_file_path,msg_box

class csv_value(Enum):

    UpDirRG = "UpDirRG"
    DwDirRG = "DwDirRG"

    UpDirSI = "UpDirSI"
    DwDirSI = "DwDirSI"

    UpDirVol = "UpDirVol"
    DwDirVol = "DwDirVol"

    Flags = "Flags"

    F_enrich = "F_enrich"
    F_enrich_sucess = "F_enrich_sucess"
    F_1ton = "F_1ton"
    F_xDpi_match = "F_xDpi_match"
    F_tethering = "F_tethering"
    F_flow_xDPI = "F_flow_xDPI"
    F_redirect = "F_redirect"
    F_signal_msg = "F_signal_msg"





def out_put_file(out_data):
    logger.debug("out_put_file")

    #csv_dir = os.path.join(sys.path[0], "csv")
    csv_dir = get_os_path("选取CSV文件将存放的目录")
    file_name = os.path.join(csv_dir, "pcap_mac.csv")
    index = 0
    while os.access(os.path.join(sys.path[0], file_name), os.R_OK) == True:
        index += 1
        name = file_name.split(".")
        inner = name[0].split("_")
        name[0] = inner[0]+"_"+inner[1] + "_"+str(index)
        file_name = (name[0] + "." + name[1])
        logger.debug("name:{0}".format(file_name))

    localtime = time.asctime(time.localtime(time.time()))
    file_name = os.path.join(csv_dir, file_name)
    print("**{0}**: **{1}** is creating.....".format(localtime, file_name))
    msg_box( "CSV 存与位置:"+file_name)

    fd = open(file_name, "w", newline='')
    csv_write = csv.writer(fd, dialect='excel')
    csv_write.writerow(['index',
                        "MobileIp", "ServerIp", "MobilePort", "ServierPort", "Protocol",
                        "DpiRuleBaseId",
                        "UpDirRG", "DwDirRG",
                        "UpdirSI", "DwDirSi",
                        "UpdirVol", "DwDirVol",
                        "Flags",
                        "F_enrich","F_enrich_sucess", "F_1ton","F_xDpi_match",
                        "F_tethering","F_flow_xDPI","F_redirect","F_signal_msg" ])

    ex_index = 0
    for (k, v) in out_data.items():
        row_list = list()

        row_list.append(ex_index)
        #logger.debug(type( k[0]) )
        #five_tuple = ( FiveTuple) k[0]
        five_tuple = k[0]
        row_list.append(five_tuple.usr_ip)
        row_list.append(five_tuple.ser_ip)
        row_list.append(five_tuple.usr_port)
        row_list.append(five_tuple.ser_port)
        row_list.append(five_tuple.net_type)

        row_list.append( k[1])

        row_list.append(v[csv_value.UpDirRG])
        row_list.append(v[csv_value.DwDirRG])

        row_list.append(v[csv_value.UpDirSI])
        row_list.append(v[csv_value.DwDirSI])

        row_list.append(v[csv_value.UpDirVol])
        row_list.append(v[csv_value.DwDirVol])

        row_list.append(v[csv_value.Flags])

        row_list.append(v[csv_value.F_enrich])
        row_list.append(v[csv_value.F_enrich_sucess])
        row_list.append(v[csv_value.F_1ton])
        row_list.append(v[csv_value.F_xDpi_match])

        row_list.append(v[csv_value.F_tethering])
        row_list.append(v[csv_value.F_flow_xDPI])
        row_list.append(v[csv_value.F_redirect])
        row_list.append(v[csv_value.F_signal_msg])

        ex_index += 1
        csv_write.writerow(row_list)

    csv_write.writerow(["附录:", ""])
    csv_write.writerow(["常用Protocol类型"," "])

    csv_write.writerow(["1", "ICMP"])
    csv_write.writerow(["2", "IGMP"])
    csv_write.writerow(["6","TCP"])
    csv_write.writerow(["17", "TCP"])

    fd.close()
