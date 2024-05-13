import logging
# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         :2024/4/27 8:45
# Author        : smart
# @File         :send_emali_base.py
# @Software     :PyCharm

#用于建立smtp连接
import smtplib
#邮箱需要专门的MIME格式
from email.mime.text import MIMEText
#支持附件
from email.mime.multipart import MIMEMultipart
#用于使用中文邮件主题
from email.header import Header
from config.config import *

def send_email(report_file):

    #读取result的内容 放到变量email_body中
    with open(report_file,encoding="utf-8")as f:
        email_body=f.read()
    #1.编写邮箱内容
    msg=MIMEMultipart()
    msg.attach(MIMEText(email_body,'html','utf-8'))
    #发件人
    msg['From']=sender
    #收件人
    msg['To']=receiver
    #邮件的标题
    msg['Subject']=Header(subject,'utf-8')


    # 上传附件
    #构造附件1，传送当前目录下的result.html 文件
    att1=MIMEText(open(report_file,'rb').read(),'base64','utf-8') #二进制格式打开
    att1["Content-Type"]='application/octet-stream'
    att1["Content-Disposition"]='attachment; filename="result.html"' #filename附件显示的名字
    msg.attach(att1)
    try:
        #连接smtp服务器并发送邮件
        smtp=smtplib.SMTP_SSL(smtp_server) #smtp服务器地址 使用SSl模式
        #登录邮箱
        smtp.login(smtp_user,smtp_ps) #发送方邮箱和授权码
        smtp.sendmail(sender,receiver,msg.as_string())
        logging.error("==============================发送邮箱成功==============================")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()

if __name__ == '__main__':
    send_email("report.html")