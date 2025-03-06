# 解码是对编码后的 URL 进行还原的一种操作，示例代码如下：
from urllib import parse
string = "%E7%88%AC%E8%99%AB"
result = parse.unquote(string)
print(result)

# url地址的拼接方式
# 1、字符串相加
baseurl = 'http://www.baidu.com/s?'
params = 'wd=%E7%88%AC%E8%99%AB'
url = baseurl + params
# 2、字符串格式化（占位符）
params = 'wd=%E7%88%AC%E8%99%AB'
url = 'http://www.baidu.com/s?%s' % params
# 3、format()方法
url = 'http://www.baidu.com/s?{}'
params = 'wd=%E7%88%AC%E8%99%AB'
url = url.format(params)