# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         :2024/5/6 17:04
# Author        : smart
# @File         :test_user_login.py
# @Software     :PyCharm
from test.case.basecase import BaseCase
class test_user_login(BaseCase):
    def test_login_success(self):
        """level1: 测试用户登录成功"""
        case_data=self.get_case_data("login_ok")
        self.send_request(case_data)

    def test_login_fail(self):
        #level2: 测试登录失败
        case_data=self.get_case_data("login_err1")
        self.send_request(case_data)