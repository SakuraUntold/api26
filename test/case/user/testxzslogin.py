import unittest
from lib import xzslogin



class MyTestCase(unittest.TestCase):
       x=xzslogin.xzs()
        #账号，密码都正确
       def test_loginok(self):
           t=self.x.xzslogin('student','123456')
           self.assertIn('成功',t)
        #账号为空，密码正确
       def test_01(self):
           def test_loginok(self):
               t = self.x.xzslogin('', '123456')
               self.assertIn('用户名或密码错误', t)
       #账号正确，密码为空
       def test_02(self):
           def test_loginok(self):
               t = self.x.xzslogin('student', '')
               self.assertIn('用户名或密码错误', t)
       #账号，密码都为空
       def test_03(self):
           def test_loginok(self):
               t = self.x.xzslogin('', '')
               self.assertIn('用户名或密码错误', t)

if __name__ == '__main__':
    unittest.main()
