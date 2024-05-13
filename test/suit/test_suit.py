# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         :2024/5/7 15:09
# Author        : smart
# @File         :test_suit.py
# @Software     :PyCharm
import unittest,sys
sys.path.append("../..")
from test.case.user.test_user_login import test_user_login
from test.case.user.test_user_reg1 import test_user_reg

smoke_suit=unittest.TestSuite()
smoke_suit.addTests([test_user_login("test_login_success"),test_user_reg("test_user_reg_ok")])

def get_suit(suit_name):
    suit_name = unittest.TestSuite()
    suit_name.addTests([test_user_login("test_login_success"),test_user_reg("test_user_reg_ok")])
    return suit_name


unittest.TextTestRunner(verbosity=2).run(smoke_suit)


