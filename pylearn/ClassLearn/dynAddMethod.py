#coding:utf-8
from types import MethodType


class NoMethodCls (object):
    pass



def MethodAdd(self, param1):
    print("i am a method add to a special object, ")
    print(param1)
   
#给类对象，运行中绑定一个方法

oNoMethodObj= NoMethodCls()
oNoMethodObj.methodAdd = MethodType(MethodAdd,oNoMethodObj)

oNoMethodObj.methodAdd("ahh")
