# coding=gbk


class Animal(object):
    pass

class Runnable(object):
    def run(self):
        print('Running...')
        
        
#���ؼ̳�
class Bat(Animal, Runnable):
    pass