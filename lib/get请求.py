import requests

url="http://httpbin.org/get"

#发送一个get请求
r=requests.get(url)

#解析一下响应对象
#响应的文本信息
print(r.text)
#响应的二进制格式
print(r.content)
#响应的编码格式
print(r.encoding)
#响应的头部信息
print(r.headers)
#响应的状态码
print(r.status_code)
# 响应的cookies值
print(r.cookies)