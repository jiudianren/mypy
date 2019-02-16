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
print("func name:")
print(now.__name__)
print(ff.__name__)

print(" ====log===== ")
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now2():
    print('2015-3-25')

print("now2 address")
print(now2)
print("now2 name")
print(now2.__name__)
print("now2() executer")
print(now2())



def now2_nolog():
    print('2015-3-25')


ff2 = log(now2)  #��log���������� 
print("\n")
print("ff2 address")
print(ff2)
print("name")
print(ff2.__name__)
print("executor")
print(ff2())
print("name")
print(now2.__name__)

print(" \n ====log2===== \n")

#����Ҫ��дwrapper.__name__ = func.__name__�����Ĵ��룬Python���õ�functools.wraps���Ǹ�����µ�
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

print("name")
print(now3.__name__)



print(" \n ====log3===== \n")
#���decorator������Ҫ�������

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

print("name")
print(now4.__name__)
print("exectuor")
now4()