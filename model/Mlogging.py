# coding=gbk
import logging

#log实例
logger = logging.getLogger('mylogger')

#创建handler 写到控制台，或者日志文件等
hds = logging.StreamHandler()

#给实例增加处理方式
logger.addHandler(hds)

#设置日志级别
logger.setLevel(logging.DEBUG)

#增加日志
logger.debug("i am debug")

def pylearnLog():
    logger = logging.getLogger("PyLearn")
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)
    return logger