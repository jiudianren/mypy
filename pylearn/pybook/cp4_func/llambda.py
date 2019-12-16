def lambda1():
    x = 10
    a = lambda y: x + y
    x = 20
    print(a(1))
lambda1()