# coding=gbk
'''
Created on 2017��7��13��

@author: Administrator
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys
def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, my main!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


print("user my module")


'''
import FunctionLearning
����ֻ��ʹ�� FunctionLearning �µ�_init_.pyģ��
'''
import FunctionLearning
FunctionLearning.FunInInit()


import FunctionLearning.ForTestImport
FunctionLearning.ForTestImport.person("UsePersion", 12,city='nanjing',heavy=172,tal='64kg')


'''
������������������helloģ���ļ�ʱ��
Python��������һ���������__name__��Ϊ__main__��
������������ط������helloģ��ʱ��if�жϽ�ʧ�ܣ�
��ˣ�����if���Կ�����һ��ģ��ͨ������������ʱִ��һЩ����Ĵ��룬
����ľ������в��ԡ�
'''
if __name__=='__main__':
    test()