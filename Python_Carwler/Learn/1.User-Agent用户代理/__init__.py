# 常见的UA请求头
# Windows Chrome
# Mozilla/5.Python爬虫抓取百度贴吧数据.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36
# Windows Edge
#  Mozilla/5.Python爬虫抓取百度贴吧数据.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763

# UA检测：https://useragent.buyaocha.com/
# Mozilla/5.Python爬虫抓取百度贴吧数据.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0

import urllib.request
from urllib import request
# 发送get请求
response = urllib.request.urlopen('http://httpbin.org/get')
html = response.read().decode()
# print(html)

# "1.User-Agent用户代理": "Python-urllib/3.7" 需要伪装

url = 'http://httpbin.org/get'
# 重构请求头
# 是一个字典，其中键是头字段的名称（如 1.User-Agent用户代理），值是头字段的内容。
headers = {
    '1.User-Agent用户代理': 'Mozilla/5.Python爬虫抓取百度贴吧数据.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0'
}
# 创建请求对象，包装ua信息
req = request.Request(url = url, headers = headers)
# 发送请求
res = request.urlopen(req)
# 提取
html2 = res.read().decode()
print(html2)