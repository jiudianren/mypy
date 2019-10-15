# coding=gbk

from model.Mlogging import pylearnLog
logger = pylearnLog()


class Bird:
    def __init__(self):
        self.hungry=True
    
    def eat(self):
        if self.hungry:
            logger.debug("a haha ")
            self.hungry=False
        else:
            logger.debug("no thanks")
            
            

class SBird(Bird):
    
    def __init__(self):
        self.song ="I am SBird"
        
    def sing(self):
        logger.debug(self.song)

#调用未关联的超类构造函数
class SBird2(Bird):
    
    def __init__(self):
        Bird.__init__(self)
        self.song ="I am SBird"
        
    def sing(self):
        logger.debug(self.song)


#调用未关联的超类构造函数
class SBird3(Bird):
    
    def __init__(self):
        super.__init__()
        self.song ="I am SBird"
        
    def sing(self):
        logger.debug(self.song)



def Test():
    
    fb =Bird()
    fb.eat()
    
    sb = SBird()
    sb.sing()
    #erro
    #sb.eat()
   
    sb2 =SBird2()
    sb2.sing()
    sb2.eat()
    
       
    sb3 =SBird3()
    sb3.sing()
    sb3.eat()
    
    
   
Test() 