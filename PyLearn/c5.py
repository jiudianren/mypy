


from math import sqrt


# 5.2
def fivePtwo ():
    x,y,z=1,2,3
    x,y=y,x
    print ( x,y)
    
    scoundrel = {'name': 'Robin', 'girlfriend': 'Marion'}
    key, value = scoundrel.popitem()
    print(key, value)


def fivePfivePSix():
    for n in range(99, 81, -1):
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
    
fivePtwo()
fivePfive()
