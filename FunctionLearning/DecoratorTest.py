# coding=gbk
'''
Created on 2017年7月13日

@author: Administrator
'''

print("function derector")
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


print("======1")

@log
def now2():
    print('2015-3-25')

print(now2)
print(now2())

ff2 = log(now2)

print("======2")
print(ff2)
print("======3")
print(ff2())

print("======3")
print(now2.__name__)

import functools
def log2(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log2
def now3():
    print('2015-3-25')


print("======4")
print(now3.__name__)


def log3(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log3("i am the text")
def now4():
    print('2015-3-25')


print("======4")
print(now4.__name__)
now4()