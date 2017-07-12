'''
Created on 2017年7月12日

@author: Lian
'''
#list list是一种有序的集合，可以随时添加和删除其中的元素
classmate=['狗蛋','毛蛋','阿毛','啊狗']
print(classmate[1])
print(classmate[-1])
classmate.append('余则成')
print (classmate[-1])
classmate.insert(1, '第一')
classmate.pop();
print(classmate[-1])


#tuple  tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字

cm=("固定","同学","元组")
print(cm)
ontMemTuple=(1,)
print(ontMemTuple)


#dict，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

print(d['Michael'])


#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复

s = set([1, 2, 3])

print(s)

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
