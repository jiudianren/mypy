# coding=gbk


'''
使用type()
首先，我们来判断对象类型，使用type()函数：


使用isinstance()
对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。


使用dir()
如果要获得一个对象的所有属性和方法，可以使用dir()函数，
它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
'''
print("dir()")
print( dir('ABC') )


class MyObject(object):
    name = 'Student'
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x 
    
    
obj = MyObject()

ret = hasattr(obj, 'x') # 有属性'x'吗？
print(ret)

ret= hasattr(obj, 'y') # 有属性'y'吗？
print(ret)

setattr(obj, 'y', 19) # 设置一个属性'y'
ret = hasattr(obj, 'y') #
print(ret) 

print("类属性和实例属性")
'''
类属性和实例属性

动态语言，可以给 实例 设置和添加属性，
所以分为类属性和示例属性
'''
obj.name="Boble"
print(obj.name)
print(MyObject.name)