# coding=gbk
import os
import sys
import time
import pdb
import logging

import  xml.dom.minidom

#logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)


#打开xml文档
dom = xml.dom.minidom.parse('Tab_Struct_PCC_SESSION.xml')

#得到文档元素对象
root = dom.documentElement

logging.debug( root.nodeName)
logging.debug( root.nodeValue)
logging.debug( root.nodeType)
logging.debug( root.ELEMENT_NODE)

root.getElementsByTagName('caption')




