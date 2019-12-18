

def show_it():
    print(range(-5,5))
    print(list(range(-5,5)))


def deal_lst():
    lst =[]
    lst += [1,2,3]
    lst.append(4)
    print(lst)
    lst.pop(2)
    print(lst)
    lst.sort()
    print(lst)
    lst.reverse()
    print(lst)


def limit():
    lst = [0,1,2,3]
    print(lst[99])
    lst[99] =10
    print(lst[99])


deal_lst()
limit()