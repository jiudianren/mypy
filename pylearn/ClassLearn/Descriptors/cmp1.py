# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/11/25 15:57

#类属性>数据描述符

#　类属性 > 数据描述符 > 实例属性 > 非数据描述符 > 找不到的属性触发__getattr__()

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


# 测试
Light.name  # 执行描述符的get内置属性
print(Light.__dict__)  # 此时的name显示的是描述符的对象


Light.name = "电灯泡"  # 没有执行描述符的set内置属性
print(Light.name)  # 输出：电灯泡
print(Light.__dict__)

del Light.name  # 没有执行描述符的delete内置属性
#print(Light.name)  # 报错，因为Light类中的name被删了
