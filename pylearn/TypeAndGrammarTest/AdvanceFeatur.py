# coding=gbk
#��Ƭ
print("��Ƭ")

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
print(L[:3])
print(L[-2:])
print('ABCDEFG'[:3])

L= list(range(10))
print(L)

# ����
print("����")
d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)
for valu in d.values():
    print(valu)
    
for key,valu in d.items():
    print(key,valu)


# �б�����ʽ
print("�б�����ʽ")
print([x * x for x in range(1, 11)])
print(range(1,11))
print( [m + n  for m in 'ABC'  for n in 'XYZ'])

#������
print('������')
#���ԣ�����б�Ԫ�ؿ��԰���ĳ���㷨����������������Ƿ������ѭ���Ĺ����в��������������Ԫ���أ������Ͳ��ش���������list��
#�Ӷ���ʡ�����Ŀռ䡣��Python�У�����һ��ѭ��һ�߼���Ļ��ƣ���Ϊ��������generator��
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
#t = (b, a + b) # t��һ��tuple
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

print("��ȡ fib2 �� returnֵ ")
g=fib2(4)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
            print('Generator return value:', e.value)
            break
        
        
#generator�ͺ�����ִ�����̲�һ����
#������˳��ִ�У�����return���������һ�к������ͷ��ء�
#�����generator�ĺ�����
#��ÿ�ε���next()��ʱ��ִ�У�����yield��䷵�أ��ٴ�ִ��ʱ���ϴη��ص�yield��䴦����ִ�С�
print('====odd(100)')
#�൱��һ��������
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


#�����Ѿ�֪��������ֱ��������forѭ�����������������¼��֣�
#һ���Ǽ����������ͣ���list��tuple��dict��set��str�ȣ�
#һ����generator�������������ʹ�yield��generator function��
#��Щ����ֱ��������forѭ���Ķ���ͳ��Ϊ�ɵ�������Iterable��
from collections import Iterable
print(isinstance([], Iterable))












