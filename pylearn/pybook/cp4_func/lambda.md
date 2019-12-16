labmda 表达式


lambda表达式的捕获变量，在执行时才会被执行

```
x= 10
a=lambda y : x+y
x=20
print(a(1))
```