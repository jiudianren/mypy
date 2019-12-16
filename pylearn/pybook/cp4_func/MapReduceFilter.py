
a=list(filter((lambda x: x> 0),range(-5,5)))
print(a)

from functools import reduce

print(reduce(lambda x,y: x+y ,range(-5,5)))