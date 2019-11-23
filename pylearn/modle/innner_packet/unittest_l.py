# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/11/22 15:20


import  unittest

'''
https://blog.csdn.net/u013378642/article/details/82386226
'''

# TestCase
class TestCase_01(unittest.TestCase):  # 继承unittest.TestCase

    @classmethod
    def setUpClass(cls):
        print('setUpClass 这是所有case的前置条件01')


    def setUp(self):
        print('setUp 这是每条case的前置条件01')


    def testThird_01(self):  # 测试用例的命名必须以test开头，否则不予执行
        print('第三条case')

    def testFirst_01(self):
        print('第一条case')

    @unittest.skip('不执行这条case')  # 跳过这条case
    def testSecond_01(self):
        print('第二条case')

    def testFourth_01(self):
        print('第四条case')

    def tearDown(self):
        print('tearDown 这是每条case的后置条件01')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass 这是所有case的后置条件01')


class TestCase_02(unittest.TestCase):  # 继承unittest.TestCase


    @classmethod
    def setUpClass(cls):
        print('setUpClass 这是所有case的前置条件02')

    def test_0201(self):
        print('02第一条case')


    @classmethod
    def tearDownClass(cls):
        print('tearDownClass 这是所有case的后置条件02')



if __name__ == '__main__':
    #TestSuite
    # unittest.main() # 使用main()直接运行时，将按case的名称顺序执行
    suite = unittest.TestSuite()

    suite.addTest(TestCase_01('test_01'))  # 将需要执行的case添加到Test Suite中，没有添加的不会被执行
    suite.addTest(TestCase_02('test_02'))  # 将需要执行的case添加到Test Suite中，没有添加的不会被执行

    #TextTestRuner
    re = unittest.TextTestRunner().run(suite)  # 将根据case添加的先后顺序执行
    # TestResult
    print(type(re))
