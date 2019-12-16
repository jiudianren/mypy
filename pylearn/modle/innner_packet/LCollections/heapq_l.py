# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/12/13 16:00


import heapq




def test_heap():

    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
    print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]

    # 按key值排序
    portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    print(cheap)
    expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
    print(expensive)



class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def __repr__(self):
        return f'queue({self._queue}),index({self._index})'


class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
print(q)
q.push(Item('bar'), 5)
print(q)
q.push(Item('spam'), 4)
print(q)
q.push(Item('spam'), 10)
print(q)
q.push(Item('grok'), 1)
print(q)



print(q.pop())
print(q)
print(q.pop())
print(q)
print(q.pop())
print(q)
print(q.pop())
print(q)
