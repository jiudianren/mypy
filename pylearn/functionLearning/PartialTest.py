# coding=gbk


print("function partial")
# ƫ����
#���ԣ����ܽ�functools.partial�����þ��ǣ�
#��һ��������ĳЩ�������̶�ס��Ҳ��������Ĭ��ֵ��������һ���µĺ�������������º�������򵥡�


#�������Ĳ�������̫�࣬��Ҫ��ʱ��ʹ��functools.partial���Դ���һ���µĺ�����
#����º������Թ̶�סԭ�����Ĳ��ֲ������Ӷ��ڵ���ʱ���򵥡�

print("use for fix some params")

import functools
int2 = functools.partial(int, base=2)
print(int2('1100'))
