# coding=gbk
import os
import sys
import time
import pdb
import logging

import  xml.dom.minidom

#logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)


#��xml�ĵ�
dom = xml.dom.minidom.parse('Tab_Struct_PCC_SESSION.xml')

#�õ��ĵ�Ԫ�ض���
root = dom.documentElement

logging.debug( root.nodeName)
logging.debug( root.nodeValue)
logging.debug( root.nodeType)
logging.debug( root.ELEMENT_NODE)

root.getElementsByTagName('caption')




