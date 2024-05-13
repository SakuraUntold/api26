# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         :2024/4/19 15:58
# Author        : smart
# @File         :db1.py
# @Software     :PyCharm
import logging

import pymysql
from config.config import *
import sys
sys.path.append('..') #提升一级到项目根目录下

def conn():
    con=pymysql.connect(host=db_host,port=db_port,
                         db=db,user=db_user,
                         password=db_ps,charset='utf8')
    return con

#封装数据库查询操作
def query_db(sql):
    con=conn()
    #创建游标
    cursor=con.cursor()
    logging.debug(sql)
    #创建游标执行sql
    cursor.execute(sql)
    #获取执行的结果
    result=cursor.fetchone()
    logging.debug(result)
    #关闭游标
    cursor.close()
    #关闭连接
    con.close()
    return result
#封装更改数据库操作
def change_db(sql):
    con = conn()
    # 创建游标
    cursor = con.cursor()
    try:
        cursor.execute(sql)
        logging.debug(sql)
        #如果成功 就提交
        con.commit()
    except Exception as e:
        logging.error(str(e))
        #如果失败 就回滚
        con.rollback()
    finally:
        cursor.close()
        con.close()

def check_user(name):
    rel=query_db("select * from t_user where user_name ='{}'".format(name))
    #三目运算符
    return True if rel else False

def add_user(name,ps):
    change_db("insert into t_user('user_name','password') values ('{}','{}')".format(name,ps))

def del_user(name):
    change_db("delete from t_user where user_name='{}'".format(name))