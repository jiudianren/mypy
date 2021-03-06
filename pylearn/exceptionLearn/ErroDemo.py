# coding=gbk


from model.Mlogging import pylearnLog
from PIL.ImImagePlugin import number

logger = pylearnLog()


def eightPfour():
    try:
        1 / 0
    except NameError:
        logger.debug("Unknown variable")
    else:
        logger.debug("That went well!")
    finally:
        logger.debug("Cleaning up.")


def DiveErro():
    try:
        print('try...')
        r = 10 / 0
        print('result:', r)
    except ZeroDivisionError as e:
        print('except:', e)
    finally:
        print('finally...')
    print('END')
    
def DiveErro2(n):
    try:
        print('try...')
        assert n != 0, 'n is zero!'    
        r = 10 / n
        print('result:', r)
    except ZeroDivisionError as e:
        print('except:', e)
    finally:
        print('finally...')
    print('END')
    

DiveErro()
DiveErro2(0)