# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         :2024/4/26 15:04
# Author        : smart
# @File         :config.py
# @Software     :PyCharm
import logging,time
import os
from optparse import OptionParser

now=time.strftime("%Y%m%d_%H%M%S", time.localtime())
tody=time.strftime("%Y-%m-%d", time.localtime())
#项目路径
prj_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path=os.path.join(prj_path,"data")
test_path=os.path.join(prj_path,"test")
test_case_path=os.path.join(prj_path,'test','case') #用例目录
log_file=os.path.join(prj_path,'log',"log{}.txt".format(tody))
report_file=os.path.join(prj_path,'report','report_{}.html'.format(now))
data_file=os.path.join(prj_path,"data","test_user_data.xlsx")
test_list_file=os.path.join(prj_path,"test","test_list.txt")
last_fails_file=os.path.join(prj_path,"last_fails.pickle")
#log文件配置
logging.basicConfig(
    level=logging.DEBUG,#用于输出一些调试信息
    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S', #日期格式
    filename=log_file,#输出日志文件
    # encoding='utf-8',
    filemode='a'
)

#数据库配置
db_host='127.0.0.1'
db_port=3306
db_user='root'
db_ps='root'
db='xzs'

#邮件配置
smtp_server='smtp.qq.com'
smtp_user='3536186591@qq.com'
smtp_ps='amxcyopboezycige'
sender=smtp_user
receiver='3536186591@qq.com'
subject="接口测试报告"
send_email_after_run=False #是否发送邮件


#命令行参数解析
parser=OptionParser()
parser.add_option("--collect-only",action="store_true",dest="collect_only",help="仅收集测试用例,不执行测试")
parser.add_option("--tag",action="store",dest="tag",default="level1",help="根据标签生成测试套件")
parser.add_option("--rerun-fails",dest="rerun_fails",action="store_true",help="重新运行失败的用例")
#生效参数
(options,args)=parser.parse_args()

if __name__ == '__main__':
    logging.info("接口测试")