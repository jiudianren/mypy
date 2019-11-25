# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/11/25 13:51


class Descriptors:
    """
    数据描述符
    """

    def __init__(self, key, expected_type):
        """
        key：          用户传进的值
        expected_type：用户传进的值的类型
        """
        self.key = key
        self.expected_type = expected_type

    """
    描述符的三个内置属性的参数如下：
    ---------------------------------------------------
    self：     是描述符的对象，不是使用描述符类的对象
    instance： 这才是使用描述符类的对象
    owner：    是instance的类
    value：    是instance的值
    ---------------------------------------------------
    """

    def __get__(self, instance, owner):
        print("执行Descriptors的get")
        return instance.__dict__[self.key]  # 将参数存入实例的字典

    def __set__(self, instance, value):
        print("执行Descriptors的%s:set"%(self.key))
        # 如果用户输入的值和值的类型不一致，则抛出TypeError异常
        if not isinstance(value, self.expected_type):
            raise TypeError("参数%s必须为%s" % (self.key, self.expected_type))
        instance.__dict__[self.key] = value  # 为实例字典的key设值

    def __delete__(self, instance):
        print("执行Descriptors的delete")
        instance.__dict__.pop(self.key)  # 删除实例字典的key


class Light:
    # 使用描述符
    name = Descriptors("name", str)
    price = Descriptors("price", float)


    def __init__(self, name, price):
        self.name = name
        self.price = price




if __name__ == "__main__":

    print(dir(Descriptors))
    print("==========")
    print(dir(Light))
    print("==========")
    reset = set(dir(Descriptors)) - set(dir(Light))
    reset2 = set(dir(Light)) - set(dir(Descriptors))
    print(reset)
    print(reset2)
    print("==========")

    # 设置两个参数，触发两次set的执行
    light = Light("电灯泡", 66.66)

    print(light.__dict__)
    light.name = "火箭筒"

    print(light.__dict__)
    """
    执行Descriptors的set
    执行Descriptors的set
    {'name': '电灯泡', 'price': 66.66}
    执行Descriptors的set
    {'name': '火箭筒', 'price': 66.66}
    """
