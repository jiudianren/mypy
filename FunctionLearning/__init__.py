# coding=gbk

'''
每一个包目录下面都会有一个__init__.py的文件，
这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包

因为__init__.py本身就是一个模块，而它的模块名就是 本包的名字 FunctionLearinig
'''


'''
在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，
有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。
'''
def FunInInit():
    print("FunctionLearinig modual ")