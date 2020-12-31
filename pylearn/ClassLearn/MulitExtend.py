# coding=utf-8

'''
Python类分为两种，一种叫经典类，一种叫新式类。都支持多继承，但继承顺序不同。
新式类：从object继承来的类。（如:class A(object)），采用广度优先搜索的方式继承（即先水平搜索，再向上搜索）。
经典类：不从object继承来的类。（如：class A()），采用深度优先搜索的方式继承（即先深入继承树的左侧，再返回，再找右侧）。

在python2中有经典类与新式类之分
在python3中没有继承任何类，那么会默认继承object类，所以python3中所有的类都是新式类,
        新式类天然具有菱形继承，因为最顶层都是object

P1(foo)    P2(foo,bar)
C1         C2(bar)
     GC(bar)


全为单继承，或者多继承只限制于对两个完全不相关的类进行联合，这个叫“mixin” "mix-ins"
MRO
'''
class P1:
    def foo(self):
        print("P1 foo")


class P2:
    def foo(self):
        print("P2 foo")

    def bar(self):
        print("P2 bar")


class C1(P1, P2):
    pass


class C2(P1,P2):
    def bar(self):
        print("C2 bar")


class GC(C1,C2):
    def bar(self):
        print("C2 bar")

if __name__ == "__main__":
    c1 = C1()
    c2 = C2()
    gc = GC()
    print(c1.foo())
    print("----------")
    print(c1.bar())
    print("----------")

    print(c2.foo())
    print("----------")
    print(c2.bar())
    print("----------")
    print("****GC:***")
    print(gc.foo())
    print("----------")
    print(gc.bar())
    print("----------")


