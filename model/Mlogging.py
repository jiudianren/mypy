# coding=gbk
import logging

#logʵ��
logger = logging.getLogger('mylogger')

#����handler д������̨��������־�ļ���
hds = logging.StreamHandler()

#��ʵ�����Ӵ���ʽ
logger.addHandler(hds)

#������־����
logger.setLevel(logging.DEBUG)

#������־
logger.debug("i am debug")

def pylearnLog():
    logger = logging.getLogger("PyLearn")
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)
    return logger