# -*- coding: UTF-8 -*-
from selenium import webdriver
import logging
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
 
 
    # log实例
logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
logger = logging.getLogger("ss")
# 创建handler 写到控制台，或者日志文件等
hds = logging.StreamHandler()
#fds = logging.FileHandler("C://Users//10259187//Desktop//Test//log.txt",mode='w', encoding='utf-8')
# 给实例增加处理方式
logger.addHandler(hds)
# 设置日志级别
# logger.setLevel(logging.WARN)
logger.setLevel(logging.DEBUG)





 
driver = webdriver.Chrome(chrome_options=options)
driver.get('http://www.baidu.com')
element = driver.find_element_by_css_selector('#su')

logger.debug(element.get_attribute('value'))
driver.quit()