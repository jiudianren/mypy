# coding=gbk


'''
ʹ��type()
���ȣ��������ж϶������ͣ�ʹ��type()������


ʹ��isinstance()
����class�ļ̳й�ϵ��˵��ʹ��type()�ͺܲ����㡣����Ҫ�ж�class�����ͣ�����ʹ��isinstance()������


ʹ��dir()
���Ҫ���һ��������������Ժͷ���������ʹ��dir()������
������һ�������ַ�����list�����磬���һ��str������������Ժͷ�����
'''
print("dir()")
print( dir('ABC') )


class MyObject(object):
    name = 'Student'
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x 
    
    
obj = MyObject()

ret = hasattr(obj, 'x') # ������'x'��
print(ret)

ret= hasattr(obj, 'y') # ������'y'��
print(ret)

setattr(obj, 'y', 19) # ����һ������'y'
ret = hasattr(obj, 'y') #
print(ret) 

print("�����Ժ�ʵ������")
'''
�����Ժ�ʵ������

��̬���ԣ����Ը� ʵ�� ���ú�������ԣ�
���Է�Ϊ�����Ժ�ʾ������
'''
obj.name="Boble"
print(obj.name)
print(MyObject.name)