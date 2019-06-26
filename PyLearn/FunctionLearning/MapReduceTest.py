# coding=gbk

#https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317852443934a86aa5bb5ea47fbbd5f35282b331335000

from collections import Iterable
from collections import Iterator
def f(x):
    return x*x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
isinstance( r, Iterator)

print( list(r))


from functools import reduce
def add(x, y):
    return x + y

ret = reduce(add, [1, 3, 5, 7, 9])
print(ret)



def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))