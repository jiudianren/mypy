# coding=gbk
#切片
print("切片")

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
print(L[:3])
print(L[-2:])
print('ABCDEFG'[:3])

L= list(range(10))
print(L)

# 迭代
print("迭代")
d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)
for valu in d.values():
    print(valu)
    
for key,valu in d.items():
    print(key,valu)


# 列表生成式
print("列表生成式")
print([x * x for x in range(1, 11)])
print(range(1,11))
print( [m + n  for m in 'ABC'  for n in 'XYZ'])

#生成器
print('生成器')
#所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，
#从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
g = (x * x for x in range(10))
L = [x * x for x in range(10)]
#python2.7
#print(g.next())
#python 3.6
print(g.__next__())
print("g is:")
print(g)
print("L is:")
print(L)
print('=====')
for n in g:
    print(n)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

# a, b = b, a + b
#t = (b, a + b) # t是一个tuple
#a = t[0]
#b = t[1]

print('====fib(100)')
fib(10)


def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

print("获取 fib2 的 return值 ")
g=fib2(4)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
            print('Generator return value:', e.value)
            break
        
        
#generator和函数的执行流程不一样。
#函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#而变成generator的函数，
#在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
print('====odd(100)')
#相当于一个生成器
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)


o=odd()
print(o)
print(next(o))
print(next(o))
print(next(o))


#我们已经知道，可以直接作用于for循环的数据类型有以下几种：
#一类是集合数据类型，如list、tuple、dict、set、str等；
#一类是generator，包括生成器和带yield的generator function。
#这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
from collections import Iterable
print(isinstance([], Iterable))












