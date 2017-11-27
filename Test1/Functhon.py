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


#可变参数
print("可变参数")
# 可变参数 自动组装成  自动组装为一个tuple
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc((1,2,3)))


def calc2( *numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc2(1,2,3))

#关键字参数

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
    
person("lisi", 12,city='nanjing',heavy=172,tal='64kg')
print("限制关键字参数")
# 命名关键字参数 只接收city和job作为关键字参数
def person2(name, age, *, city, job):
    print(name, age, city, job)

# 命名关键字 参数

def person3(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person3('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
    
    
f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

#最神奇的是通过一个tuple和dict，你也可以调用上述函数：
print("组合参数")
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)

#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
#这5种参数都可以组合使用。但是请注意，
#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数