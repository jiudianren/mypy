# coding=gbk

from model.Mlogging import pylearnLog
import abc
logger = pylearnLog()
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
    "the doc about Student"
    
    #print将会在第一次实例化的时候被执行
    print("before define Student")
    #belong to all instance of the student
    time  = 0 
    #构造函数
    def __init__(self,name,score,address):
        logger.debug("__init__")
        
        Student.time+=1
        
        self.name=name
        self.score=score
        #__表示私有变量
        self.__privateVal=address
    
    #析构函数
    #也称作析构函数（destructor）。这个方法在对象被销毁
    #（作为垃圾被收集）前被调用，但鉴于你无法知道准确的调用时间，建议尽可能不要使用__del__
    def __del__(self):
        logger.debug("__del__")
        
    def printStu(self):
        self.__printImp()
        


#私有方法
    def __printImp(self):
        print(' __printImp : name:',self.name,"score",self.score,"address",self.__privateVal)
        
    def cPrint(self):
        print("I am student's cprint:")


class MiddlerSchoolStu(Student):
    
        #重写构造函数
        #todo
        #。为此，有两种方法：调用未关联的超类构造函数，以及使用函数super。接下来的两节将介绍这两种方法。
        def __init__(self):
            
        #重写
        def __printImp(self):
            print('MiddlerSchoolStu  __printImp : name:',\
                  self.name,"score",self.score,"address",self.__privateVal)
        



def cPrint():
    print("I am gloabl cPrint")


logger.debug( help(Student))
temp=80
LStu=Student("李三",temp,"sanlitun")
logger.debug("print(LStu):")
logger.debug(LStu)
logger.debug("print(Student)")
logger.debug(Student)

LStu.printStu()
logger.debug(Student.printStu(LStu))

temp=90
LStu.printStu()

logger.debug(LStu.name)
#print(LStu.__privateVal)

logger.debug("cannt change the private var")
LStu.__privateVal="tiananmen"

logger.debug( LStu.__privateVal )
LStu.printStu()


logger.debug("属性 ，函数 和方法")

LStu.cPrint()

myPrint = LStu.cPrint
myPrint()

#可以用函数替换类的方法， 
#可以理解为方法，就是绑定了第一个参数为self的函数

LStu.cPrint = cPrint
LStu.cPrint()

logger.debug("类的 命名空间")

logger.debug(Student.time)
logger.debug(LStu.time)

newstu=Student("new", 10,"address")
logger.debug(LStu.time)
logger.debug(newstu.time)


logger.debug("继承")

class Filter:
    def __init__(self):
        self.block=[]
    def filter(self,squence):
        return [x for x in squence if x not in self.block ]


class SPFilter(Filter):
    def __init__(self, block):
        self.block = block
        
        

f = Filter()
logger.debug( f.filter([1,2,3]))

sf=SPFilter("SP")
logger.debug( sf.filter( ["a", "b", "SP", "SY"]))

logger.debug(sf.__class__)
logger.debug( issubclass(SPFilter,Filter))
logger.debug( SPFilter.__base__)
logger.debug( Filter.__base__)


logger.debug("多重继承")

#必须在class语句中小心排列这些超类，因为位于前面的类的方法将覆盖位于后面的类的方法。



logger.debug("接口和内省")

class Talker:
    
    def talk(self):
        logger.debug(" hi ,my value is", self.value)
        

tk = Talker()
logger.debug(hasattr( tk,"talk"))
logger.debug(callable( getattr(tk, "talk")))



logger.debug("抽象类")


from  abc import ABC, abstractmethod

#logger.debug( help(abc))
#logger.debug(help(ABC))

logger.debug(help(abstractmethod))
             
             
class ABTalk(ABC):
    @abstractmethod
    def talk(self):
        pass
    



#继承


 
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




