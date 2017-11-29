# coding=gbk

# 高阶函数
print(abs(-10))
print(abs)
f=abs
print(f)


#abs=10
#print(abs(10))


def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))


print("filter")
print(filter)

def is_odd(n):
    return n % 2 == 1

print( list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])) )


print("sorted")
print(sorted)
ret = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(ret)

