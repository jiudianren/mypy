# coding=gbk


class Animal(object):
    pass

class Runnable(object):
    def run(self):
        print('Running...')
        
        
#多重继承
class Bat(Animal, Runnable):
    pass