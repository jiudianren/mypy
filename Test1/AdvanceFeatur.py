# coding=gbk
#��Ƭ
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
print(L[:3])
print(L[-2:])
print('ABCDEFG'[:3])

# ����

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)
for valu in d.values():
    print(valu)
    
for key,valu in d.items():
    print(key,valu)


# �б�����ʽ
print([x * x for x in range(1, 11)])
print(range(1,11))
print( [m + n for m in 'ABC' for n in 'XYZ'])

#������
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


#�൱��һ��������
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


#�����Ѿ�֪��������ֱ��������forѭ�����������������¼��֣�
#һ���Ǽ����������ͣ���list��tuple��dict��set��str�ȣ�
#һ����generator�������������ʹ�yield��generator function��
#��Щ����ֱ��������forѭ���Ķ���ͳ��Ϊ�ɵ�������Iterable��
from collections import Iterable
print(isinstance([], Iterable))












