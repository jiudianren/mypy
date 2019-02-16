from math import sqrt
from model.Mlogging import pylearnLog

logger = pylearnLog()
  
# 5.2
def fivePtwo ():
    x,y,z=1,2,3
    x,y=y,x
    print ( x,y)
    
    scoundrel = {'name': 'Robin', 'girlfriend': 'Marion'}
    key, value = scoundrel.popitem()
    print(key, value)


def fivePfivePSix():
    for n in range(99, 27, 81, -1):
        root = sqrt(n)
        if root == int(root):
            print(n)
            break
    else:
        print("Didn't find it!")

def fivePfive():
    names =["a","b","c"]
    age =[1,2,3]

    print(list(zip(names,age)) )
    
    strings=["a","b","xxx",'c']
    for index, string in enumerate(strings):
        if 'xxx' in string:
            strings[index] = '[censored]'
    
    
    fivePfivePSix()


def fivePsix():
    
    girls = ['alice', 'bernice', 'clarice']
    boys = ['chris', 'arnold', 'bob']
    rs = [b+'+'+g for b in boys for g in girls if b[0] == g[0]]
    print(rs)

def fivePseven():
    x = 30
    #删除的仅仅是名称
    del x
    y = ["hello", "world"]
    x=y
    x[1] = "python"
    del y
    print( x)


fivePtwo()
fivePfive()
fivePsix()
fivePseven()

