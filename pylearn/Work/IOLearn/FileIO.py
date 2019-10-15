# coding=gbk
 
fileHandle=open('./FileOpera.txt', 'r')
 
try:
    all_the_text = fileHandle.read( )
    print(all_the_text)
    fileHandle.append(all_the_text)
finally:
    fileHandle.close( )