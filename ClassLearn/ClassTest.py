# coding=gbk
'''
Created on 2017��7��13��

@author: Lian
'''

'''
ע�⵽__init__�����ĵ�һ��������Զ��self����ʾ������ʵ������
��ˣ���__init__�����ڲ����Ϳ��԰Ѹ������԰󶨵�self��
��Ϊself��ָ�򴴽���ʵ������
'''


'''
��Python�У�����������__xxx__�ģ�Ҳ������˫�»��߿�ͷ��������˫�»��߽�β�ģ�
�������������������ǿ���ֱ�ӷ��ʵģ�
����private���������ԣ�������__name__��__score__�����ı�����

'''


'''
˫�»��߿�ͷ��ʵ�������ǲ���һ�����ܴ��ⲿ�����أ���ʵҲ���ǡ�
����ֱ�ӷ���__name����ΪPython�����������__name�����ĳ���_Student__name��
���ԣ���Ȼ����ͨ��_Student__name������__name������
'''
class Student:
    def __init__(self,name,score,address):
        self.name=name
        self.score=score
        #__��ʾ˽�б���
        self.__privateVal=address
    
    def printStu(self):
        print('name:',self.name,"score",self.score,"address",self.__privateVal)
        


temp=80
LStu=Student("����",temp,"sanlitun")
print("print(LStu)")
print(LStu)

print("print(Student)")

print(Student)
LStu.printStu()
temp=90
LStu.printStu()

print(LStu.name)
#print(LStu.__privateVal)

print("cannt change the private var")
LStu.__privateVal="tiananmen"

print( LStu.__privateVal )
LStu.printStu()




'''
��̬���� vs ��̬����

����Ƕ�̬���Եġ�Ѽ�����͡���������Ҫ���ϸ�ļ̳���ϵ��
һ������ֻҪ����������Ѽ�ӣ�����·����Ѽ�ӡ���
�����Ϳ��Ա�������Ѽ�ӡ�

��������  run_twice ��������Ҫ��һ�� animal���ͣ�
ʵ���ϣ�ֻҪ����һ�� ����run�����Ķ���Ϳ����ˣ�
�������� һ��animal

'''
def run_twice(animal):
    animal.run()
    animal.run()




