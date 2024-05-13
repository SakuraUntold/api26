# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         :2024/5/7 8:59
# Author        : smart
# @File         :test_user_reg1.py
# @Software     :PyCharm
from test.case.basecase import BaseCase
from lib.db1 import *
import json

class test_user_reg(BaseCase):

    def test_user_reg_ok(self):
        #注册用户
        case_data=self.get_case_data("reg_ok")
        username=json.loads(case_data["args"])["userName"]
        #环境检查
        if check_user(username):
            del_user(username)
        self.send_request(case_data)
        #数据库断言
        self.assertTrue(check_user(username))
        #数据清理
        del_user(username)

    def test_user_reg_fail(self):
        #注册用户
        case_data = self.get_case_data("reg_err")
        name = json.loads(case_data["args"])["userName"]
        # 环境检查
        if not check_user( name):
            add_user( name,"123456")
        self.send_request(case_data)
        # SQL数据库断言
        self.assertTrue(check_user( name))

