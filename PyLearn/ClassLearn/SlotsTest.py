# coding=gbk


print("��̬�󶨷���")


class Student(object):
    pass

s=Student()

def set_age(self, age): # ����һ��������Ϊʵ������
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s) # ��ʵ����һ������
s.set_age(25) # ����ʵ������
ret=s.age # ���Խ��

print(ret)

#ʹ��__slots__
print("slots")

'''
Ϊ�˴ﵽ���Ƶ�Ŀ�ģ�Python�����ڶ���class��ʱ��
����һ�������__slots__�����������Ƹ�classʵ������ӵ����ԣ�
ʹ��__slots__Ҫע�⣬__slots__��������Խ��Ե�ǰ��ʵ�������ã��Լ̳е������ǲ������õģ�
'''

class Student2(object):
    __slots__ = ('name', 'age') 

s = Student2() # �����µ�ʵ��
s.name = 'Michael' # ������'name'
s.age = 25 # ������'age'
#s.score = 99 # ������'score'
