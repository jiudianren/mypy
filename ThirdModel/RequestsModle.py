# coding=gbk
import requests
import logging

#���� ��������ģ��
logging.basicConfig(level=logging.DEBUG)

r = requests.get('https://www.douban.com/') # ������ҳ
r.status_code
logging.debug(r.text)
