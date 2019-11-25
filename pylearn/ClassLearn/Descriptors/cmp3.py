# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/11/25 16:07
#实例属性 >非 数据描述符

class Descriptors:
    """
    非数据描述符
    """

    def __get__(self, instance, owner):
        print("执行Descriptors的set")

    def __delete__(self, instance):
        print("执行Descriptors的delete")


class Light:
    # 使用描述符
    name = Descriptors()

    def __init__(self, name, price):
        self.name = name
        self.price = price


# 测试
light = Light("电灯泡", 60)  # 报错，描述符中没有__set__()方法
