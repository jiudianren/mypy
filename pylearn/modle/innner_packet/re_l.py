# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/11/22 14:56

import re


class MyRe(object):
    re_modle = 1

    def find_num(self, in_str):
        '''
        :param in_str:
        :return:
        找到所有的数字 整数 小数 包括负数
        '''
        modle = self.re_modle
        lst = re.findall(r"\d", in_str)
        print(lst)
        lst = re.findall(r"\d+", in_str)
        print(lst)
        return lst


if __name__ == "__main__":
    pass
