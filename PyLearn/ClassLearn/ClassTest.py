# coding=gbk

from model.Mlogging import pylearnLog
import abc
logger = pylearnLog()
'''
Created on 2017��7��13��

@author: Lian
'''

'''
ע�⵽__init__�����ĵ�һ��������Զ��self����ʾ������ʵ��������
��ˣ���__init__�����ڲ����Ϳ��԰Ѹ������԰󶨵�self��
��Ϊself��ָ�򴴽���ʵ��������
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
    "the doc about Student"
    
    #print�����ڵ�һ��ʵ������ʱ��ִ��
    print("before define Student")
    #belong to all instance of the student
    time  = 0 
    #���⺯�� __xx__
    #���캯�� 
    def __init__(self,name,score,address):
        logger.debug("__init__")
        
        Student.time+=1
        
        self.name=name
        self.score=score
        #__��ʾ˽�б���
        self.__privateVal=address
    
    #��������
    #Ҳ��������������destructor������������ڶ�������
    #����Ϊ�������ռ���ǰ�����ã����������޷�֪��׼ȷ�ĵ���ʱ�䣬���龡���ܲ�Ҫʹ��__del__
    def __del__(self):
        logger.debug("__del__")
        
    def printStu(self):
        self.__printImp()


    #˽�з���
    def __printImp(self):
        print(' __printImp : name:',self.name,"score",self.score,"address",self.__privateVal)
        
    def cPrint(self):
        print("I am student's cprint:")

    #�������� ͨ�� Student.no_self_param_func()���þͿ�����
    def no_self_param_func():
        print("no_self_param_func")
        

class MiddlerSchoolStu(Student):
    #��д���캯��
    #todo
    #Ϊ�ˣ������ַ���������δ�����ĳ��๹�캯�����Լ�ʹ�ú���super�������������ڽ����������ַ�����
    def __init__(self):
        pass
            
    #��д
    def __printImp(self):
        print('MiddlerSchoolStu __printImp: name:', self.name,"score",self.score,"address",self.__privateVal)
        



def cPrint():
    print("I am gloabl cPrint")


logger.debug( help(Student))
temp=80
LStu=Student("����",temp,"sanlitun")
logger.debug("print(LStu):")
logger.debug(LStu)
logger.debug("print(Student)")
logger.debug(Student)

LStu.printStu()
logger.debug(Student.printStu(LStu))

logger.debug(Student.no_self_param_func())

##ֱ�ӷ���˽�з���
logger.debug("derector visit the private func")
LStu._Student__printImp()

temp=90
LStu.printStu()

logger.debug(LStu.name)
#print(LStu.__privateVal)

logger.debug("cannt change the private var")
LStu.__privateVal="tiananmen"

logger.debug( LStu.__privateVal )
LStu.printStu()

logger.debug("���� ������ �ͷ���")

LStu.cPrint()

myPrint = LStu.cPrint
myPrint()

#�����ú����滻��ķ�����  ��������Ϊ���������ǰ��˵�һ������Ϊself�ĺ���

LStu.cPrint = cPrint
LStu.cPrint()

logger.debug("��� �����ռ�")

logger.debug(Student.time)
logger.debug(LStu.time)

newstu=Student("new", 10,"address")
logger.debug(LStu.time)
logger.debug(newstu.time)


logger.debug("�̳�")

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


logger.debug("���ؼ̳�")

#������class�����С��������Щ���࣬��Ϊλ��ǰ�����ķ���������λ�ں������ķ�����



logger.debug("�ӿں���ʡ")

class Talker:
    
    def talk(self):
        logger.debug(" hi ,my value is", self.value)
        

tk = Talker()
logger.debug(hasattr( tk,"talk"))
logger.debug(callable( getattr(tk, "talk")))



logger.debug("������")


from  abc import ABC, abstractmethod

#logger.debug( help(abc))
#logger.debug(help(ABC))

logger.debug(help(abstractmethod))
             
             
class ABTalk(ABC):
    @abstractmethod
    def talk(self):
        pass
    



#�̳�



class Rectangle:
    def __init__ (self):
        self.width = 0
        self.height = 0
    def set_size(self, size):
        self.width, self.height = size
    def get_size(self):
        return self.width, self.height
    size = property(get_size, set_size)
   

def testProperty():
    
    rectan = Rectangle()
    rectan.width=10
    rectan.height=5
    logger.debug(rectan.size)
    rectan.size =12,15
    logger.debug(rectan.size)
    


logger.debug("��̬�������෽��")

class MyClass:
    
    @staticmethod
    def smeth():
        print('This is a static method')
    @classmethod
    def cmeth(cls):
        print('This is a class method of', cls)

logger.debug(MyClass.cmeth())
logger.debug(MyClass.smeth())



    
 
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



