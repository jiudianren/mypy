# coding=gbk
'''
Created on 2017年7月13日

@author: Lian
'''

class student:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    
    def printStu(self):
        print('name:',self.name,"score",self.score)
        

LStu=student("李三",80)
LStu.printStu()