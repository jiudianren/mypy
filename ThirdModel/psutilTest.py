# coding=gbk
import psutil 
import logging

#process and system utilities
logging.basicConfig(level=logging.DEBUG)

rs=psutil.disk_partitions() # ���̷�����Ϣ
logging.debug(rs)
psutil.disk_usage('/') # ����ʹ�����
psutil.disk_io_counters() # ����IO
