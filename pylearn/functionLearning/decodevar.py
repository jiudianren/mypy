# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/12/13 13:50



records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]
def do_foo(x, y):
    print('foo', x, y)
def do_bar(s):
    print('bar', s)

for it in records:
    pass
    #print(it)

for tag, *args in records:
    #print(tag,*args)
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


def de_1():
    record = ('ACME', 50, 123.45, (12, 18, 2012))
    name, *_, (*_, year) = record
    print(name, year)

de_1()

#保留最后的有几个元素
import collections
def search(lines, pattern, history=5):
    previous_lines = collections.deque(maxlen=history)
    for line in lines:
        if line%pattern == 0:
            print("yield")
            yield line, previous_lines
        previous_lines.append(line)


for it, de in search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,15,16],2 ):
    print(it,de)