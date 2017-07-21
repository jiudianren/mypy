# coding=gbk
#切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
print(L[:3])
print(L[-2:])
print('ABCDEFG'[:3])

# 迭代

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)
for valu in d.values():
    print(valu)
    
for key,valu in d.items():
    print(key,valu)


# 列表生成式
print([x * x for x in range(1, 11)])
print(range(1,11))
print( [m + n for m in 'ABC' for n in 'XYZ'])

#生成器
g = (x * x for x in range(10))
print(g.next())

for n in g:
    print(n)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(100)


#相当于一个生成器
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)


o=odd
print(next(o))
print(next(o))
print(next(o))


#我们已经知道，可以直接作用于for循环的数据类型有以下几种：
#一类是集合数据类型，如list、tuple、dict、set、str等；
#一类是generator，包括生成器和带yield的generator function。
#这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
from collections import Iterable
print(isinstance([], Iterable))












