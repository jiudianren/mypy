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
