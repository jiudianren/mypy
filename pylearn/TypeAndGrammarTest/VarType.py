# coding=gbk
'''
Created on 2017��7��12��

@author: Lian
'''
#list list��һ������ļ��ϣ�������ʱ��Ӻ�ɾ�����е�Ԫ��
classmate=['����','ë��','��ë','����']
print(classmate[1])
print(classmate[-1])
classmate.append('�����')
print (classmate[-1])
classmate.insert(1, '��һ')
classmate.pop();
print(classmate[-1])


#tuple  tuple��list�ǳ����ƣ�����tupleһ����ʼ���Ͳ����޸ģ�����ͬ�����г�ͬѧ������

cm=("�̶�","ͬѧ","Ԫ��")
print(cm)
ontMemTuple=(1,)
print(ontMemTuple)


#dict��dictȫ��dictionary��������������Ҳ��Ϊmap��ʹ�ü�-ֵ��key-value���洢�����м���Ĳ����ٶ�

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

print(d['Michael'])


#set��dict���ƣ�Ҳ��һ��key�ļ��ϣ������洢value������key�����ظ�

s = set([1, 2, 3])

print(s)

#set���Կ�����ѧ�����ϵ���������ظ�Ԫ�صļ��ϣ���ˣ�����set��������ѧ�����ϵĽ����������Ȳ�����
