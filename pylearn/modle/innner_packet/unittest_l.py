# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/11/22 15:20


import  unittest

'''
https://blog.csdn.net/u013378642/article/details/82386226
https://www.cnblogs.com/xiaoxiaolvdou/p/9503090.html
https://docs.python.org/2/library/unittest.html

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


def http_run():
    fp = open(os.getcwd() + "/test_report.html", "wb")
    runner = HTMLTestRunner(stream=fp,
                            title="测试报告标题",
                            description="测试报告描述信息",
                            tester="测试者")
    runner.run(s)



def text_runner():
    #TestSuite
    # unittest.main() # 使用main()直接运行时，将按case的名称顺序执行
    suite = unittest.TestSuite()

    #TestCase_01('testFirst_01') 测试用例类名（“测试的方法”）
    suite.addTest(TestCase_01('testFirst_01'))  # 将需要执行的case添加到Test Suite中，没有添加的不会被执行
    suite.addTest(TestCase_02('test_0201'))  # 将需要执行的case添加到Test Suite中，没有添加的不会被执行

    #TextTestRuner
    runer = unittest.TextTestRunner()  # 将根据case添加的先后顺序执行
    re = runer.run(suite)
    # TestResult
    print(type(re))


if __name__ == '__main__':
    text_runner()
