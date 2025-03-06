# 首先我们对要编写的爬虫程序进行简单地分析，该程序可分为以下三个部分：
#     拼接 url 地址
#     发送请求
#     将照片保存至本地

# 爬旮旯给木

from urllib import request
from urllib import parse
import os

# 拼接url地址
def get_url(word):
    url = 'https://www.hikarinagi.com/?s={}'
    # 使用urlencode编码
    params = parse.urlencode({'wd': word})
    url = url.format(params)
    return url

# 发请求,保存本地文件
def request_url(url, filename):
    # 请求对象 + 响应对象 + 提取内容
    headers = {'User-Agent' : 'Mozilla/5.Python爬虫抓取百度贴吧数据.0 (compatible; MSIE 9.0; Windows NT 6.re模块用法.1; Trident/5.Python爬虫抓取百度贴吧数据.0'}
    req = request.Request(url=url, headers=headers)
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    # 保存文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"文件已保存到: {os.path.abspath(filename)}")


# 主程序入口
if __name__ == '__main__':
  word = input('请输入搜索内容:')

  print("当前工作目录:", os.getcwd())
  filename = word + '.html'
  file_path = os.path.join(os.getcwd(), filename)
  print("文件保存路径:", file_path)

  url = get_url(word)
  filename = word + '.html'
  request_url(url,filename)