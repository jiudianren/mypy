# coding=gbk
'''
Created on 2017��7��13��

@author: Lian
'''

class student:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    
    def printStu(self):
        print('name:',self.name,"score",self.score)
        

LStu=student("����",80)
LStu.printStu()