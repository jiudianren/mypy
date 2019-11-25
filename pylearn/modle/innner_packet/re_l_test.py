# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/11/22 15:29


import  unittest
from re_l import MyRe


class Test_Re_l_01(unittest.TestCase):  # 继承unittest.TestCase

    @classmethod
    def setUpClass(cls):
        print('setUpClass 这是所有case的前置条件 \n')
        myre= MyRe()

    def setUp(self):
        print('setUp 这是每条case的前置条件\n')

    def test_1(self):
        print('第一条case \n')

    @unittest.skip('不执行这条case \n')  # 跳过这条case
    def test_2(self):
        print('第二条case \n')

    def test_find_num_01(self):  # 测试用例的命名必须以test开头，否则不予执行
        print('find_num 正整数 \n')
        num_str = "1a"
        re = Test_Re_l_01.myre.find_num(num_str)

    def test_4(self):
        print('第四条case \n')


    def tearDown(self):
        print('tearDown 这是每条case的后置条件\n')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass 这是所有case的后置条件\n')


class Test_Re_l_02(unittest.TestCase):  # 继承unittest.TestCase
    def test_02_01(self):
        print('02 第一条case \n')




if __name__ == '__main__':
    unittest.main(verbosity=2)
    # unittest.main() # 使用main()直接运行时，将按case的名称顺序执行
    suite = unittest.TestSuite()

    suite.addTest(Test_Re_l_01('test_lpf'))  # 将需要执行的case添加到Test Suite中，没有添加的不会被执行
    suite.addTest(Test_Re_l_02('test_re'))
    #suite.addTest(Test_Re_l_01('testFirst_01'))
    re   = unittest.TextTestRunner().run(suite)  # 将根据case添加的先后顺序执行
