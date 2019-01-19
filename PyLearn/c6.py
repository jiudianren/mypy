from model.Mlogging  import pylearnLog


logger=pylearnLog()
  


def hello(name):
    " NOTE about this func hello"
    return "heelo"+name

def SixpOne():
    print(hello.__doc__)
    print( hello("world"))

#不可变参数
def pConst(str,num,tu):
    str ="new world"
    num = 100
    tu =(1,2,3)
    print(str,num,tu)

def testPconst():
    str = "out world"
    num =1
    tu=(3,2,1)
    print(str,num,tu)
    pConst(str, num ,tu)
    print(str,num,tu)

def pRef( ref):
    ref[0] = "changed"


def testPRef():
    ref=["changeing", "ornot"]
    print(ref)
    pRef(ref)
    print(ref)
    
def pFour(): 
    testPconst()
    testPRef()
    
    
hello.__doc__  
SixpOne()

pFour()