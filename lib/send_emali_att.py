#用于建立smtp连接
import smtplib
#邮箱需要专门的MIME格式
from email.mime.text import MIMEText
#支持附件
from email.mime.multipart import MIMEMultipart
#用于使用中文邮件主题
from email.header import Header
#读取result的内容 放到变量email_body中
with open("result.html",encoding="utf-8")as f:
    email_body=f.read()
#1.编写邮箱内容
msg=MIMEMultipart()
msg.attach(MIMEText(email_body,'html','utf-8'))
#发件人
msg['From']='3536186591@qq.com'
#收件人
msg['To']='3536186591@qq.com'
#邮件的标题
msg['Subject']=Header('星期六怎末还上课')


# 上传附件
#构造附件1，传送当前目录下的result.html 文件
att1=MIMEText(open('result.html','rb').read(),'base64','utf-8') #二进制格式打开
att1["Content-Type"]='application/octet-stream'
att1["Content-Disposition"]='attachment; filename="result.html"' #filename附件显示的名字
msg.attach(att1)



#连接smtp服务器并发送邮件
smtp=smtplib.SMTP_SSL('smtp.qq.com') #smtp服务器地址 使用SSl模式
#登录邮箱
smtp.login('3536186591@qq.com','amxcyopboezycige') #发送方邮箱和授权码
smtp.sendmail('3536186591@qq.com','3536186591@qq.com',msg.as_string())
smtp.quit()