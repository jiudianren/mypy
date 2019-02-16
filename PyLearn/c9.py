# coding=gbk

from model.Mlogging import pylearnLog
logger = pylearnLog()

def check_index(key):

    if not isinstance(key, int): raise TypeError
    if key < 0: raise IndexError
    
class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {} # 没有任何元素被修改
    
    def __getitem__(self, key):
            """
            从算术序列中获取一个元素
            """
            check_index(key)
            try: return self.changed[key] # 修改过？
            except KeyError: # 如果没有修改过，
                return self.start + key * self.step # 就计算元素的值

    def __setitem__(self, key, value):
        """
        修改算术序列中的元素
        """
        check_index(key)
        self.changed[key] = value # 存储修改后的值
        
        
    def test(self):
        slf =ArithmeticSequence(1,2)
        logger.debug(slf[4])
        slf[2]="two"
        logger.debug(slf[2])
        #del slf[3]
        #slf[-1] 
        #slf["foure"]


class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0
    
    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)


        
ArithmeticSequence(1,2).test()


#9.5.1


      