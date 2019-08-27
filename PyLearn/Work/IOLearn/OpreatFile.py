# coding=gbk

import os
print(os.name)
# print( os.uname )
print( os.environ )

'''
操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，
这一点要注意一下。
查看、创建和删除目录可以这么调用：
'''
# 查看当前目录的绝对路径:
print( os.path.abspath('.') )

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
print(os.path.join('./', 'testdir') ) 
print( os.path.split('/Users/michael/testdir/file.txt') )
print( os.path.splitext('/path/to/file.txt'))
# 删掉一个目录:
os.rmdir('./pymakepath')
# 然后创建一个目录:
os.mkdir('./pymakepath')

try:
    os.rename('./test.txt', 'test.txt1')
except FileNotFoundError as e:
    print(e)
    os.rename('test.txt1','test.txt')
    
# os.mknod("aha.txt")  
with open('./aha.txt', 'w+') as f:
    print(f.write("ss"))  
    print(f.read())
    
os.remove('aha.txt')

#列举所有目录
print(os.listdir('.') )
aa=[x for x in os.listdir('.') if os.path.isdir(x)]
print(aa)

bb =[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(bb)

