# 函数式编程


##偏函数

import functools
int2 = functools.partial(int, base=2)
int2('1000000')
64
