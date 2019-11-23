# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/11/22 14:56

import re
import unittest





def find_num(in_str):
    '''

    :param in_str:
    :return:
    找到所有的数字 整数 小数 包括负数
    '''
    rlst = re.findall("\d", in_str)
    print(rlst)
    rlst = re.findall("\d+", in_str)
    print(rlst)
    return rlst


def main():
    num_str = "1a10b-2c0.5d,"
    find_num(num_str)


if __name__ == "__main__":

    main()
