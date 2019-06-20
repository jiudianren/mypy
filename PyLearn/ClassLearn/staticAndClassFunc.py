# coding=gbk



from model.Mlogging import pylearnLog
logger = pylearnLog()




class  Computer(object):
    
    
    def  __init__():
        pass
    
    
    
    @staticmethod
    def systemtype():
        print(" it is a linux ")
        
        
    @classmethod
    def mysystemtype(cls):
        print("it is a ubantu system")
        
        
def TestCpt():

    Computer.mysystemtype()
    Computer.systemtype()
        
if __name__ == "__main__" :
    TestCpt

