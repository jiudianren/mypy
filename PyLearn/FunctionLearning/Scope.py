# coding=gbk


from model.Mlogging import pylearnLog
from PIL.ImImagePlugin import number


def funcScope():
    x =1
    scope= vars()
    print(scope['x'])
    
    
funcScope()