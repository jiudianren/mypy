

# 如何理解

https://blog.konghy.cn/2017/04/24/python-entry-program/

#  1

    const.py
    PI = 3.14

    def main():
        print "PI:", PI

    main()
    
    
    
    cal.py
    from const import PI

    def calc_round_area(radius):
        return PI * (radius ** 2)

    def main():
        print "round area: ", calc_round_area(2)

    main()
    
    ----print PI
    ----print round area
    

#  2

    const.py
    PI = 3.14

    def main():
        print "PI:", PI
  
    if __name__ == "__main__":
      main()
    
   
    
    cal.py
    from const import PI

    def calc_round_area(radius):
        return PI * (radius ** 2)

    def main():
        print "round area: ", calc_round_area(2)

    main()
   
    ----print round area
    
    
    
    
    4. __main__.py文件与python -m
Python的-m参数用于将一个模块或者包作为一个脚本运行，而__main__.py文件相当于是一个包的“入口程序“。

4.1 运行Python程序的两种方式
python xxx.py，直接运行xxx.py文件
python -m xxx.py，把xxx.py当做模块运行
假设我们有一个文件run.py，内容如下：

import sys

print(sys.path)
1
2
3
我们用直接运行的方式启动

python run.py
1
输出结果(为了说明问题，输出结果只截取了重要部分，下同)：

['/home/huoty/aboutme/pythonstudy/main', ...]
1
然后以模块的方式运行:

python -m run.py
1
输出内容

['', ...]
/usr/bin/python: No module named run.py
1
2
由于输出结果只列出了关键的部分，应该很容易看出他们之间的差异：

直接运行方式是把run.py文件所在的目录放到了sys.path属性中

以模块方式运行是把你输入命令的目录（也就是当前工作路径），放到了 sys.path 属性中。

以模块方式运行还有一个不同的地方：多出了一行No module named run.py的错误。实际上以模块方式运行时，Python先对run.py执行一遍 import，所以print(sys.path)被成功执行，然后Python才尝试运行run.py模块，但是在path变量中并没有run.py这个模块，所以报错。正确的运行方式，应该是python -m run。

    
    4.2 __main__.py的作用
仍然先看例子，假设我们有如下一个包package：

package
├── __init__.py
└── __main__.py
1
2
3
其中，文件__init__.py的内容

import sys

print("__init__")
print(sys.path)
1
2
3
4
其中，文件__main__.py的内容

import sys

print("__main__")
print(sys.path)
1
2
3
4
接下来，我们运行这个package，使用python -m package运行，输出结果：

__init__
['', ...]

__main__
['', ...]
1
2
3
4
5
使用python package运行，输出结果：

__main__
['package', ...]
1
2
总结一下

当加上-m参数时，Python会把当前工作目录添加到sys.path中；而不加-m时，Python则会把脚本所在目录添加到sys.path中。

当加上-m参数时，Python会先将模块或者包导入，然后再执行。

__main__.py文件是一个包或者目录的入口程序。不管是用python package还是用python -m package运行，__main__.py文件总是被执行。
    
