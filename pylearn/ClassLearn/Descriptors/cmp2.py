# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/11/25 16:03

'''
　数据描述符 > 实例属性
在以下实验中，数据描述符的优先级大于实例属性的优先级，
此时实例属性name被数据描述符所覆盖，
而price没有描述符代理，所以它任然是实例属性

'''
class Descriptors:
    """
    数据描述符
    """

    def __get__(self, instance, owner):
        print("执行Descriptors的get")

    def __set__(self, instance, value):
        print("执行Descriptors的set")

    def __delete__(self, instance):
        print("执行Descriptors的delete")


class Light:
    # 使用描述符
    name = Descriptors()

    def __init__(self, name, price):
        self.name = name
        self.price = price


# 使用类的实例对象来测试
light = Light("电灯泡", 60)  # 执行描述符的set内置属性
light.name  # 执行描述符的get内置属性
print(light.__dict__)  # 查看实例的字典，不存在name
print("====")
print(Light.__dict__)  # 查看类的字典，存在name（为描述符的对象）
del light.name  # 执行描述符的delete内置属性
