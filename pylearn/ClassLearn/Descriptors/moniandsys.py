# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/11/25 16:09

class Imitate_classmethod:
    """
        使用描述符模拟@classmethod
"""

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        # 对传进函数进行加工,最后返回该函数
        def machining_func(*args, **kwargs):
            print("函数加工处理后，返回实例的类")
            return self.func(owner, *args, **kwargs)

        return machining_func


class Test:
    book_name = "从你的世界路过"

    # 使用装饰器的结果等价于将函数变为属性:
    # book = Imitate_classmethod( book )
    @Imitate_classmethod
    def book_1(cls):
        print("这本书的名字是：%s" % cls.book_name)

    @Imitate_classmethod
    def book_2(cls, price):
        print("这本书的名字是：%s；价格是 %s" % (cls.book_name, price))


# 测试
Test.book_1()
Test.book_2(28.5)
"""
运行输出：
---------------------------------------------
函数加工处理后，返回实例的类
这本书的名字是：从你的世界路过
函数加工处理后，返回实例的类
这本书的名字是：从你的世界路过；价格是 28.5
---------------------------------------------
"""





class Imitate_property:
    """
    使用描述符模拟property
    """

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        # 回调传入的函数，将运行结果保存在变量res中
        res = self.func(instance)
        # 为函数名func.__name__设置一个值res后存入对象的字典中
        setattr(instance, self.func.__name__, res)
        return res


class Test_pro:

    def __init__(self, value):
        self.value = value

    @Imitate_property
    def function(self):
        return self.value ** 2


test = Test_pro(2)
print(test.function)  # 输出：4
print(test.__dict__)  # 输出：{'value': 2, 'function': 4}
print(test.function)  # 输出：4
print(test.function)  # 输出：4
print(test.__dict__)  # 输出：{'value': 2, 'function': 4}





class Imitate_staticmethod:
    """
    使用描述符模拟@staticmethod
    """

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        # 对传进函数进行加工,最后返回该函数
        def machining_func(*args, **kwargs):
            print("函数加工处理后，返回实例的类")
            return self.func(*args, **kwargs)

        return machining_func


class Test_staticmethod:

    @Imitate_staticmethod
    def static_func(*args):
        print("您输入的是：", *args)


# 测试
Test_staticmethod.static_func("柠檬", "香蕉")
test = Test_staticmethod()
test.static_func(110, 112)
"""
运行输出：
-------------------------------------------------------------------
函数加工处理后，返回实例的类
您输入的是： 柠檬 香蕉
函数加工处理后，返回实例的类
您输入的是： 110 112
-------------------------------------------------------------------
"""




class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))


    @classmethod
    def class_foo(cls, x):
        print ("executing class_foo(%s,%s)" % (cls, x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)



a = A()
a.foo(1)
# executing foo(<__main__.A object at 0xb7dbef0c>,1)
a.class_foo(1)
# executing class_foo(<class '__main__.A'>,1)
A.class_foo(1)
# executing class_foo(<class '__main__.A'>,1)
a.static_foo(1)
# executing static_foo(1)
A.static_foo('hi')
# executing static_foo(hi)


'''
通过上述验证我们发现：

foo()的调用者必须是类A的一个实例，class_foo()与static_foo()的调用者既可以是类也可以是某个实例
参数不同，foo() 参数为self和其他参数，class_foo()参数使用类（cls）替换了self，static_foo()则只有参数，没有self和类(cls)
a.foo(1)中的foo()与a是绑定的，class_foo()是与类绑定的，而static_foo()与这两者都没有绑定

@property
作用：
将类方法转换为只读属性
重新实现一个属性的setter和getter方法
'''
