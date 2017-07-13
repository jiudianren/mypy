# coding=gbk
'''
Created on 2017年7月13日

@author: Administrator
'''

# 装饰器
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

# 偏函数
#所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
import functools
int2 = functools.partial(int, base=2)
print(int2('1100'))

