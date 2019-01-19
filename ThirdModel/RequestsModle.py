# coding=gbk
import requests
import logging

#处理 网络请求模块
logging.basicConfig(level=logging.DEBUG)

r = requests.get('https://www.douban.com/') # 豆瓣首页
r.status_code
logging.debug(r.text)
