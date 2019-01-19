# coding=gbk


print("动态绑定方法")


class Student(object):
    pass

s=Student()

def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
ret=s.age # 测试结果

print(ret)

#使用__slots__
print("slots")

'''
为了达到限制的目的，Python允许在定义class的时候，
定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
'''

class Student2(object):
    __slots__ = ('name', 'age') 

s = Student2() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
#s.score = 99 # 绑定属性'score'
