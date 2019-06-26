# coding=gbk
#类中有些方法可以 自定义，定义了这些方法，类就可以实现系统的一些功能
#这些方法中包括  __iter__  __repr__() __str__ 等等

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__
    
s=Student('Michael')
print(s  )
s



#迭代器


class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
        
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
    
    def __iter__(self):
        return self