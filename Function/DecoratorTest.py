# coding=gbk
'''
Created on 2017��7��13��

@author: Administrator
'''

print("function derector")
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


print("======1")
@log
def now2():
    print('2015-3-25')

print(now2)
print(now2())

ff2 = log(now2)