# coding=gbk

import os
print(os.name)
# print( os.uname )
print( os.environ )

'''
�����ļ���Ŀ¼�ĺ���һ���ַ���osģ���У�һ���ַ���os.pathģ���У�
��һ��Ҫע��һ�¡�
�鿴��������ɾ��Ŀ¼������ô���ã�
'''
# �鿴��ǰĿ¼�ľ���·��:
print( os.path.abspath('.') )

# ��ĳ��Ŀ¼�´���һ����Ŀ¼�����Ȱ���Ŀ¼������·����ʾ����:
print(os.path.join('./', 'testdir') ) 
print( os.path.split('/Users/michael/testdir/file.txt') )
print( os.path.splitext('/path/to/file.txt'))
# ɾ��һ��Ŀ¼:
os.rmdir('./pymakepath')
# Ȼ�󴴽�һ��Ŀ¼:
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

#�о�����Ŀ¼
print(os.listdir('.') )
aa=[x for x in os.listdir('.') if os.path.isdir(x)]
print(aa)

bb =[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(bb)

