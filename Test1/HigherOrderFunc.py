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
