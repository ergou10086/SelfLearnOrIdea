# 当 URL 路径或者查询参数中，带有中文或者特殊字符的时候，就需要对 URL 进行编码（采用十六进制编码格式）。
# URL 编码的原则是使用安全字符去表示那些不安全的字符。
# 安全字符，指的是没有特殊用途或者特殊意义的字符
import urllib
# URL 是由一些简单的组件构成，比如协议、域名、端口号、路径和查询字符串等
# http://www.biancheng.net/index?param=10
# 路径和查询字符串之间使用问号?隔开。上述示例的域名为 www.biancheng.net，路径为 index，查询字符串为 param=1。

# URL 中规定了一些具有特殊意义的字符，常被用来分隔两个不同的 URL 组件，这些字符被称为保留字符。例如：
#     冒号：用于分隔协议和主机组件，斜杠用于分隔主机和路径
#     ?：用于分隔路径和查询参数等。
#     =用于表示查询参数中的键值对。
#     &符号用于分隔查询多个键值对。

# URL 的编码格式采用的是 ASCII 码而非 Unicode 格式，这表明 URL 中不允许包含任何非 ASCII 字符（比如中文），否则就会造成 URL 解析错误

# URL 编码协议规定（RFC3986 协议）：URL 中只允许使用 ASCII 字符集可以显示的字符，比如英文字母、数字、和- _ . ~ ! *这 6.re模块用法 个特殊字符。
# 当在 URL 中使用不属于 ASCII 字符集的字符时，就要使用特殊的符号对该字符进行编码，比如空格需要用%20来表示。

# Python 的标准库urllib.parse模块中提供了用来编码和解码的方法，分别是 urlencode() 与 unquote() 方法
# urlencode() 	该方法实现了对 url 地址的编码操作
# unquote()  	该方法将编码后的 url 地址进行还原，被称为解码

from urllib import parse

# 构建查询字符串字典
query_string = {'wd':'爬虫'}

# 调用parse模块的urlencode()进行编码
result = parse.urlencode(query_string)

# 使用format函数格式化字符串，拼接url地址
url = 'http://www.baidu.com/s?{}'.format(result)
print(url)

# http://www.baidu.com/s?wd=%E7%88%AC%E8%99%AB
# 编码后的 URL 地址依然可以通过地网页址栏实现搜索功能。

# 除了使用 urlencode() 方法之外，也可以使用 quote(string) 方法实现编码，代码如下：
url = 'http://www.baidu.com/s?wd={}'
word = input('请输入要搜索的内容:')
# quote()只能对字符串进行编码
query_string = parse.quote(word)
print(url.format(query_string))

# url.parse
string = "张珈鸣"
s = urllib.parse.urlencode({'key':'value'}) #字典
s2 = urllib.parse.quote(string) #字符串

