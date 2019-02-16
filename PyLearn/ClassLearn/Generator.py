# coding=gbk

from model.Mlogging import pylearnLog
logger = pylearnLog()


g = ((i + 2) ** 2 for i in range(2, 27))
logger.debug(next(g))
logger.debug(next(g))


def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element
            


nested = [[1, 2], [3, 4], [5]]

logger.debug( next(flatten(nested)))


#递归式生成器
def flatten2(nested):
    try:
        for sublist in nested:
            for element in flatten2(sublist):
                yield element
    except TypeError:
        yield nested
        
        
def flatten3(nested):
    try:
        # 不迭代类似于字符串的对象：
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten3(sublist):
                yield element
    except TypeError:
        yield nested
    
logger.debug(list(flatten2([[[1], 2], 3, 4, [5, [6, 7]], 8])))
logger.debug( list(flatten3(['foo', ['bar', ['baz']]])) )
