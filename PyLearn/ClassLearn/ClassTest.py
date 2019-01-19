# coding=gbk
'''
Created on 2017年7月13日

@author: Lian
'''

'''
注意到__init__方法的第一个参数永远是self，表示创建的实例本身，
因此，在__init__方法内部，就可以把各种属性绑定到self，
因为self就指向创建的实例本身。
'''


'''
在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，
是特殊变量，特殊变量是可以直接访问的，
不是private变量，所以，不能用__name__、__score__这样的变量名

'''


'''
双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
所以，仍然可以通过_Student__name来访问__name变量：
'''
class Student:
    def __init__(self,name,score,address):
        self.name=name
        self.score=score
        #__表示私有变量
        self.__privateVal=address
    
    def printStu(self):
        print('name:',self.name,"score",self.score,"address",self.__privateVal)
        


temp=80
LStu=Student("李三",temp,"sanlitun")
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
静态语言 vs 动态语言

这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，
一个对象只要“看起来像鸭子，走起路来像鸭子”，
那它就可以被看做是鸭子。

比如这里  run_twice 看着像是要求一个 animal类型，
实际上，只要传入一个 具有run方法的对象就可以了，
不必须是 一个animal

'''
def run_twice(animal):
    animal.run()
    animal.run()




