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


# �ɱ���� �Զ���װ�� dicts
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
    
person("lisi", 12,city='nanjing',heavy=172,tal='64kg')
# �����ؼ��ֲ��� ֻ����city��job��Ϊ�ؼ��ֲ���
def person2(name, age, *, city, job):
    print(name, age, city, job)
    
#��Python�ж��庯���������ñ�ѡ������Ĭ�ϲ������ɱ�������ؼ��ֲ����������ؼ��ֲ�����
#��5�ֲ������������ʹ�á�������ע�⣬
#���������˳������ǣ���ѡ������Ĭ�ϲ������ɱ�����������ؼ��ֲ����͹ؼ��ֲ���