import json
import unittest,requests
from lib import read_excel
from lib.db1 import *
from lib.case_log import log_case_info



class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) :
        cls.r = read_excel.readexcel()
        cls.l = cls.r.excel_to_list(data_file, "test_user_reg")
    def test_reg_ok(self):

        reg1=self.r.get_test_data(self.l,"reg_ok")
        print(reg1)
        url=reg1.get("url")
        #获取到的是个字符串格式
        args=reg1.get("args")
        res=reg1.get("expect_res")
        #将字符串转成字典
        a=json.loads(args)
        #获取提交参数中的username值
        name=a.get("userName")
        #在数据库中做比对，如果数据库中有就删除
        if check_user(name):
            del_user(name)
        r=requests.post(url,json=a)
        #
        log_case_info("test_reg_ok",url,a,res,r.text)
        #
        self.assertIn(res,r.text)
        #测试完成后 还原数据
        del_user(name)

    def test_reg_err(self):
        reg1 = self.r.get_test_data(self.l, "reg_err")
        print(reg1)
        url = reg1.get("url")
        # 获取到的是个字符串格式
        args = reg1.get("args")
        res = reg1.get("expect_res")
        # 将字符串转成字典
        a = json.loads(args)

        r = requests.post(url, json=a)
        # logging.debug("测试用例: {}".format("test_reg_err"))
        # logging.info("url: {}".format(url))
        # logging.info("请求参数：{}".format(args))
        # logging.info("期望结果: {}".format(res))
        # logging.info("实际结果： {}".format(r.text))
        log_case_info("test_reg_err",url,a,res,r.text)
        self.assertIn(res, r.text)



if __name__ == '__main__':
    unittest.main(verbosity=2)
