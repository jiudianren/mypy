# coding=gbk

a= abs
print(a(-1))


def my_abs(x):
    if not isinstance(x, (int, float)):
        print("not right")
#     raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-100))


def nop():
    pass

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
def cal(*numbers):
    summ=0
    for n in numbers:
        summ=summ+n*n
    return summ

nummm={1,2,3,4,5}

print(cal(*nummm))


# 可变参数 自动组装成 dicts
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
    
person("lisi", 12,city='nanjing',heavy=172,tal='64kg')
# 命名关键字参数 只接收city和job作为关键字参数
def person2(name, age, *, city, job):
    print(name, age, city, job)
    
#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
#这5种参数都可以组合使用。但是请注意，
#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数