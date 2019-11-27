# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/11/22 15:29


import  unittest
from re_l import MyRe


class Test_Re_l_01(unittest.TestCase):  # 继承unittest.TestCase

    my_re = MyRe()

    @classmethod
    def setUpClass(cls):
        print('setUpClass 这是所有case的前置条件 \n')

    def setUp(self):
        print('setUp 这是每条case的前置条件\n')

    @unittest.skip('不执行这条case \n')  # 跳过这条case
    def test_2(self):
        print('第二条case \n')

    def test_find_num_01(self):  # 测试用例的命名必须以test开头，否则不予执行
        print('find_num 正整数 \n')
        re_true = [100,]
        num_str = "100a"
        re = self.my_re.find_num(num_str)
        self.assertEqual(re, re_true)

        re_true = [100,]
        num_str = "bca100"
        re = self.my_re.find_num(num_str)
        self.assertEqual(re, re_true)

        re_true = [100, ]
        num_str = "bca100bas"
        re = self.my_re.find_num(num_str)
        self.assertEqual(re, re_true)

    def test_find_num_02(self):
        print('find_num 负整数 \n')
        re_true = [-100, ]
        num_str = "b-100a"
        re = self.my_re.find_num(num_str)
        print(f"{re_true}---{re}")
        self.assertEqual(re, re_true)


    def test_find_num_03(self):
        print('find_num 小数 \n')
        re_true = [2.15,-2.15 ]
        num_str = "b2.15a-2.15"
        re = self.my_re.find_num(num_str)
        print(f"{re_true}--{re}")
        self.assertEqual(re, re_true)

    def test_find_num_04(self):
        print('find_num all \n')
        re_true = [1, 211, -200, 12.34, -12.34, 55]
        num_str = "1a211b-200c12.34d-12.34f55"
        re = self.my_re.find_num(num_str)
        print(f"{re_true}--{re}")
        self.assertEqual(re, re_true)

    def test_get_ip_01(self):
        print('get_ip  \n')
        re_true = ["192.255.15.1",]
        re = self.my_re.get_ip_v4("aaa192.255.15.1abasdfa")
        print(f"{re_true}--{re}")
        self.assertEqual(re, re_true)

    def test_get_ip_03(self):
        print('get_ip  \n')
        re_true = ["1.2.3.4", "191.1.254.44", "255.255.255.255"]
        re = self.my_re.get_ip_v4("1.2.3.4aaa191.1.254.44abasdfas255.255.255.255")
        print(f"{re_true}--{re}")
        self.assertEqual(re, re_true)

    def test_get_ip_02(self):
        print('get_ip  \n')
        re_true = []
        re = self.my_re.get_ip("aa1000.20.30.40")
        print(f"{re_true}--{re}")
        self.assertEqual(re, re_true)



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
