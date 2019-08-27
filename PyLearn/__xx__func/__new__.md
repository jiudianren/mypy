https://blog.csdn.net/sj2050/article/details/81172022

class CapStr(str):
    def __init__(self,string):
        string = string.upper()
 
a = CapStr("I love China!")
print(a)



class CapStr(str):
    def __new__(cls,string):
        string = string.upper()
        return super().__new__(cls,string)
 
a = CapStr("I love China!")
print(a)
