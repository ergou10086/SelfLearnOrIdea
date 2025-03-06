# requests.get()
# 该方法用于 GET 请求，表示向网站发起请求，获取页面响应对象
# res = requests.get(url,headers=headers,params,timeout)
# 参数说明如下：
#     url：要抓取的 url 地址。
#     headers：用于包装请求头信息。
#     params：请求时携带的查询字符串参数。
#     timeout：超时时间，超过时间会抛出异常。

# requests.post()
# 该方法用于 POST 请求，先由用户向目标 url 提交数据，然后服务器返回一个 HttpResponse 响应对象
# response=requests.post(url,data={请求体的字典})

import requests
import ssl
print(ssl.OPENSSL_VERSION)

# 百度翻译
url = 'https://osu.ppy.sh/beatmapsets'
# post请求体携带的参数，可通过开发者调试工具查看,查看步骤：NetWork选项->Headers选项->Form Data
# 如果 data 是一个字典，requests 会将其编码为 application/x-www-form-urlencoded 格式，并作为请求体发送。
'''
data = {
    'q': 'Tao Hua Xiao',
    's': 'ranked',
    'm': '0',
    'sort': 'title_asc',
    'nsfw': 'true'
}
'''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Referer': 'https://osu.ppy.sh/beatmapsets'
}

response = requests.post(url, headers=headers)
print(response.text)

print(response.encoding)
response.encoding="utf-8"    #更改为utf-8编码
print(response.status_code)  # 打印状态码
print(response.url)          # 打印请求url
print(response.headers)      # 打印头信息
print(response.cookies)      # 打印cookie信息
print(response.text)  #以字符串形式打印网页源码
print(response.content) #以字节流形式打印