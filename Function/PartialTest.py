# coding=gbk


print("function partial")
# ƫ����
#���ԣ����ܽ�functools.partial�����þ��ǣ���һ��������ĳЩ�������̶�ס��Ҳ��������Ĭ��ֵ��������һ���µĺ�������������º�������򵥡�
import functools
int2 = functools.partial(int, base=2)
print(int2('1100'))
