# coding=gbk
import logging
#PIL ����ͼƬģ��
from PIL import Image,ImageFilter
logging.info("here")
im = Image.open("jiangren.PNG")
w,h=im.size
logging.info("here")
logging.info("siez %s %s" %(w,h))
logging.info("here")

im2=im.filter(ImageFilter.BLUR)
im2.save("jiangren2.PNG")
logging.info("ok")