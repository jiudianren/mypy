# coding=gbk

print("�ݹ麯��====start")

#β�ݹ���ָ���ں������ص�ʱ�򣬵������������ң�return��䲻�ܰ������ʽ��
#���������������߽������Ϳ��԰�β�ݹ����Ż���
#ʹ�ݹ鱾�����۵��ö��ٴΣ���ֻռ��һ��ջ֡���������ջ����������

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

ret=fact(10)
print(ret)

print("�ݹ麯��====end")