# coding=gbk

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

import logging

def main2():
    try:
        bar('0')
    except ZeroDivisionError as e:
        logging.exception(e)
        print('ZeroDivisionError:', e)
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')


import pdb

s = '0'
n = int(s)
# will into pdb env to debug the program
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)

main2()
main()