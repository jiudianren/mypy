from model.Mlogging  import pylearnLog


logger=pylearnLog()
  


def hello(name):
    " NOTE about this func hello"
    return "hello "+name

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
    
def pFourPTwo():
    
    names = ['Mrs. Entity', 'Mrs. Thing']
    n = names # 再次假装传递名字作为参数
    n[0] = 'Mr. Gumby' # 修改列表
    logger.debug(names)
    
    logger.debug("is " )
    logger.debug((n is names)) 
    logger.debug("== ") 
    logger.debug((n == names)) 
    
    n2=names[:]
    logger.debug("is " )
    logger.debug((n2 is names)) 
    logger.debug("== ") 
    logger.debug((n2 == names)) 
   
    
def pFour(): 
    pFourPTwo()
    testPconst()
    testPRef()
    
    
hello.__doc__  
SixpOne()

pFour()