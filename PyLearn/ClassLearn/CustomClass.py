# coding=gbk
#������Щ�������� �Զ��壬��������Щ��������Ϳ���ʵ��ϵͳ��һЩ����
#��Щ�����а���  __iter__  __repr__() __str__ �ȵ�

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__
    
s=Student('Michael')
print(s  )
s



#������


class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
        
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
    
    def __iter__(self):
        return self