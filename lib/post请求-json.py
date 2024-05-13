# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time         :2024/4/15 15:35
# Author        : smart
# @File         :post请求-json.py
# @Software     :PyCharm
import requests

url="http://httpbin.org/post"

data='''{
    "name":"zhangsan",
    "age":"18"
}''' #多行文本，字符串格式，也可以单行（注意外层有引号，为字符串）data=
'{ "name":"zhangsan","age":"18"}'

r=requests.post(url=url,data=data)
print(r.text)

#参数写在字典里
data = {"name": "马斯克","age": 45}
 #请求时将字典参数赋给data参数
response = requests.post("http://httpbin.org/post", data=data)
 #打印响应
print(response.text)