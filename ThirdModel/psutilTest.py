# coding=gbk
import psutil 
import logging

#process and system utilities
logging.basicConfig(level=logging.DEBUG)

rs=psutil.disk_partitions() # 磁盘分区信息
logging.debug(rs)
psutil.disk_usage('/') # 磁盘使用情况
psutil.disk_io_counters() # 磁盘IO
