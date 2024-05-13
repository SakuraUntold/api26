import unittest

def setUpModule(): #当前模块执行前只执行一次
    print('=== setUpmodule ===')
def tearDownModule(): #当前模块执行后只执行一次
    print('=== tearDownmodule ===')

class MyTestCase(unittest.TestCase):
    #在所有的用例执行之前 只运行一次
    @classmethod
    def setUpClass(cls) -> None:
        print('setupclass')
        #在所有的用例执行之后 都会运行一次
    @classmethod
    def tearDownClass(cls):
        print('teardownclass')
    #在每个用例执行之前都会运行一次
    def setUp(self):
        print('setup')
    #在每个用例执行之后都会运行一次
    def tearDown(self):
        print('teardown')

    #所有的测试用例必须以test开头
    def test_01(self):
        print('test01')
        #比较值相等
        self.assertEqual(True,True)

    def test_02(self):
        print('test02')
        #包含  a包含在b中
        self.assertIn('h','hello')

    def test_03(self):
        print('test03')
        #比较内存中的位置
        self.assertIsNot(2,4/2)

    def test_04(self):
        print('test04')
        #比大小 less<  greater >  lessequal <=  greaterequal >=
        self.assertGreater(7,4)

    def test_05(self):
        print('test05')
        #判断类型
        self.assertIsInstance([1,2,3],list)




if __name__ == '__main__':
    unittest.main()
