# coding=gbk
'''
Created on 2017��7��13��

@author: Administrator
'''

# װ����
def now():
    print('2015-3-25')
    
ff=now
print(now.__name__)
print(ff.__name__)


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now2():
    print('2015-3-25')

print(now2)
print(now2())

ff2 = log(now2)
print(ff2)
print(ff2())

# ƫ����
#���ԣ����ܽ�functools.partial�����þ��ǣ���һ��������ĳЩ�������̶�ס��Ҳ��������Ĭ��ֵ��������һ���µĺ�������������º�������򵥡�
import functools
int2 = functools.partial(int, base=2)
print(int2('1100'))

