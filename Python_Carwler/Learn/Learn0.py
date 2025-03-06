# 向百度（http://www.baidu.com/）发起请求，获取百度首页的 HTML 信息

import urllib.request
response = urllib.request.urlopen('https://www.amoebi.com/')
# <http.client.HTTPResponse object at 0x0000020790372AC8>
print(response)

# 提取响应内容
html = response.read().decode('utf-8')
print(html)

# urlopen()
# 表示向网站发起请求并获取响应对象

# Request()
# 该方法用于创建请求对象、包装请求头，比如重构 1.User-Agent用户代理（即用户代理，指用户使用的浏览器）使程序更像人类的请求，而非机器。重构 1.User-Agent用户代理 是爬虫和反爬虫斗争的第一步。
# urllib.request.Request(url.headers)

bytes = response.read()  # read()返回结果为 bytes 数据类型
string = response.read().decode()  # decode()将字节串转换为 string 类型
url = response.geturl()  # 返回响应对象的URL地址
code = response.getcode()  # 返回请求时的HTTP响应码
