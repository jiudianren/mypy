# coding=gbk

#元类

#动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。

def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)


'''
type()函数依次传入3个参数：
class的名称；
继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
'''

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
h = Hello()
h.hello()

'''
metaclass
除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
'''