# coding=gbk


from model.Mlogging import pylearnLog
from PIL.ImImagePlugin import number

logger = pylearnLog()

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

# Ĭ�ϲ���
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi/6)
logger.debug( (x,y))





#�ɱ����
print("�ɱ����")

def calc(numbers):
    sum = 0
    for n in numbers:
        logger.debug("�ɱ����:%d " % n)
        sum = sum + n * n
    return sum

#�൱�� ������һ��tuple 
print(calc( (1,2,3) ))

# �ɱ���� �Զ���װ��  �Զ���װΪһ��tuple
def calc2( *numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print( calc2(1,2,3) )

#�ؼ��ֲ���
print("�ؼ��ֲ���")

def person(name, age, **kw):
    "parm ** is a dict"
    print('name:', name, 'age:', age, 'other:', kw)
    
person("lisi", 12,city='nanjing',heavy=172,tal='64kg')


# �����ؼ��ֲ���   ֻ����city��job��Ϊ�ؼ��ֲ���
print("�����ؼ��ֲ���")
def person2(name, age, *, city, job):
    print(name, age, city, job)


def person3(name, age, **kw):
    if 'city' in kw:
        # ��city����
        pass
    if 'job' in kw:
        # ��job����
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person3('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


def f1(a, b, c=0, *args, **kw):
    print('f1 a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('f2 a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
    
    
f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

#���������ͨ��һ��tuple��dict����Ҳ���Ե�������������
print("��ϲ���")
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)

#��Python�ж��庯���������ñ�ѡ������Ĭ�ϲ������ɱ�������ؼ��ֲ����������ؼ��ֲ�����
#��5�ֲ������������ʹ�á�������ע�⣬
#���������˳������ǣ���ѡ������Ĭ�ϲ������ɱ�����������ؼ��ֲ����͹ؼ��ֲ���