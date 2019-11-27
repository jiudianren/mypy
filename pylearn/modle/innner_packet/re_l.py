# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/11/22 14:56

import re

'''
常用正则表达式
https://www.cnblogs.com/jinjiangongzuoshi/p/4820077.html
'''

'''
+   一次到多次

\w  字符
\b  零宽断言


前项否等模式需要理解
'''

class MyRe(object):
    re_modle = 1

    def forword_not(self):
        '''

            上面学习前向搜索或后向搜索模式(?=pattern)，这个模式里看到有等于号=，
            它是表示一定相等，其实前向搜索模式里，还有不相等的判断。

            比如你需要识别EMAIL地址：noreply@example.com，这个EMAIL地址大多数是不需要回复的，
            所以我们要把这个EMAIL地址识别出来，并且丢掉它。怎么办呢？这时你就需要使用前向搜索否定模式，
            它的语法是这样：(?!pattern)，这里的感叹号就是表示非，不需要的意思。
            比如遇到这样的字符串：noreply@example.com，
            它会判断noreply@是否相同，如果相同，就丢掉这个模式识别，不再匹配
            :return:
        '''
        address = re.compile(
            '''
            ^
            # An address: username@domain.tld
            # Ignore noreply addresses
            (?!noreply@.*$)
            [\w\d.+-]+       # username
            @
            ([\w\d.]+\.)+    # domain name prefix
            (com|org|edu)    # limit the allowed top-level domains
            $
            ''',
            re.VERBOSE)

        candidates = [
            u'first.last@example.com',
            u'noreply@example.com',
        ]

        for candidate in candidates:
            print('Candidate:', candidate)
            match = address.search(candidate)
            if match:
                print('  Match:', candidate[match.start():match.end()])
            else:
                print('  No match')

    def forword_backword(self):
        '''

        :return:
        https://blog.csdn.net/lilongsy/article/details/78505309

        \b 零宽断言，匹配一个单词边界，单词被定义为 Unidcode 的字母数字或下横线字符
            举个栗子：\bFishC\b 会匹配字符串 "love FishC"、FishC." 或 "(FishC)"

        '''
        str ="I'm singing while you're dancing."

        #前向搜索肯定模式(?=exp) 匹配exp前面的位置
        lst  = re.findall(r"\b\w+(?=ing\b)", str)
        print(f"1 {lst}")

        # 前向搜索否定模式 (?！exp) 匹配后面跟的不是exp的位置
        str ="1 12 123 4321 12345"
        #\d{3}(?!\d)匹配三位数字，而且这三位数字的后面不能是数字；
        lst = re.findall("\d{3}(?!\d)",str)
        print(f"2 {lst}")

        str = "ing wing  bbing aaaing dddding"
        lst = re.findall("\w{3}(?!ing)", str)
        print(f"2 {lst}")

        # 后向搜索肯定模式 (?<=exp)
        str ="I'm ingaa ing  while you're dancing ingdnn."
        lst = re.findall(r"(?<=ing)\w+\b", str)
        print(f"3 {lst}")

        # 后向搜索否定模式 (?<!exp)
        str = "I'm ingaa ing  while you're dancing ingdnn."
        lst = re.findall(r"(?<!ing)\w+\b", str)
        print(f"4 {lst}")


    def get_ip_v4(self, str):
        #          (([01]\d\d|2[0-4]\d|25[0-5]\d)\.){3}([01]\d\d|2[0-4]\d|25[0-5]\d)
        #(?:...) 非捕获组，即该子组匹配的字符串无法从后边获取
        re_str = r"((?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d]))"
        lst = re.findall(re_str,str)

        print(f"get_ip {lst}")
        return lst

    def find_num(self, in_str):
        '''
        :param in_str:
        :return:
        找到所有的数字 整数 小数 包括负数
        # \d 数字
        # \. 转义.
        # ? 匹配前面的子表达式零次或一次，等价于 {0,1}

        #* 0次或多次
        # \- 转义 -
        # | 或者 A|B A或者B
        '''

        #re提取文本中的浮点值，包括整数，小数，科学计数法
        re_float = r"-?\d+\.?\d*e?-?\d*?"
        lst =re.findall(re_float,in_str)
        print(lst)
        lst = [ float(x) for x in lst]
        return lst

def test():

    myre =MyRe()
    myre.forword_backword()
    myre.forword_not()
    myre.get_ip_v4("1.2.3.4ad255.0.241.0aaa100.101.102.255bb10.20.255.255")


if __name__ == "__main__":
    pass
    test()