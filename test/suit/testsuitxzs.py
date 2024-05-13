import unittest,time
from test.case.user.test_xzs_reg import MyTestCase as regtest
from test.case.user.testxzslogin import MyTestCase as logintest
from lib.HTMLTestRunner import HTMLTestRunner
from config.config import *

class MyTestCase(unittest.TestCase):
    def test_suit(self):
        #创建了一个测试套件
        suit=unittest.TestSuite()
        #添加单个的用例
        suit.addTest(regtest("test_reg_ok"))
        #添加多个的测试用例
        suit.addTests([logintest("test_loginok"),
                       logintest("test_01"),logintest("test_02"),
                       logintest("test_03")])
        unittest.TextTestRunner(verbosity=2).run(suit)

    def test_makesuit(self):
        #makessuit 单个用例
        suit1=unittest.makeSuite(regtest,"test_reg_ok")
        #会将整个测试方法都添加到suit2中
        suit2=unittest.makeSuite(logintest)
        #将两个测试集 suit1 suit2 整合成一个suit5
        suit5=unittest.TestSuite([suit1,suit2])
        # unittest.TextTestRunner(verbosity=2).run(suit1)
        #生成文本格式的测试报告
        with open(report_file,"w")as f:
            unittest.TextTestRunner(verbosity=2,stream=f).run(suit5)

    def test_loader(self):
        #loader 加载该测试类所有用例并生成测试集
        suit3=unittest.TestLoader().loadTestsFromTestCase(logintest)
        #生成HTML格式的测试报告
        with open(report_file,"wb")as f:
            HTMLTestRunner(
                stream=f,
                title="xzs登录用例",
                description='xzs登录用例集',
                verbosity=2
            ).run(suit3)

    # def test_discover(self):
    #     #discover 遍历当前目录及子包中所有test_*。py中所有unittest用例
    #     suit4=unittest.TestLoader().discover("./")
    #     unittest.TextTestRunner(verbosity=2).run(suit4)
    #





if __name__ == '__main__':
    unittest.main()
