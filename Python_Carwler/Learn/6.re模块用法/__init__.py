# 使用 re 正则解析模块实现网页信息的提取。

# 正则表达式的基本语法
# .：匹配任意单个字符
# \d：匹配数字，\D：匹配非数字字符。
# \w：匹配字母、数字或下划线，\W：匹配非字母、数字或下划线的字符
# \s：匹配空白字符（空格、制表符、换行符等），\S：匹配非空白字符。
# []：匹配括号内的任意一个字符（例如 [abc] 匹配 a、b 或 c）。
# ^：匹配字符串的开头。
# $：匹配字符串的结尾。
# *：匹配前面的字符 0 次或多次。
# +：匹配前面的字符 1 次或多次。
# ?：匹配前面的字符 0 次或 1 次。
# {n}：匹配前面的字符恰好 n 次。
# {n,}：匹配前面的字符至少 n 次。
# {n,m}：匹配前面的字符至少 n 次，至多 m 次。

# re.match(pattern, string) 功能：从字符串的开头匹配正则表达式。
# re.search(pattern, string) 功能：在字符串中搜索第一个匹配正则表达式的子串
# re.findall(pattern, string) 功能：查找字符串中所有匹配正则表达式的子串。返回一个列表，包含所有匹配的子串。
# re.sub(pattern, repl, string) 功能：将字符串中匹配正则表达式的部分替换为指定的字符串。返回替换后的字符串。
# re.compile()  该方法用来生成正则表达式对象，其语法格式如下：regex=re.compile(pattern,flags=0)
# re.split()  该函数使用正则表达式匹配内容，切割目标字符串。返回值是切割后的内容列表。

# 匹配对象的方法
# 当使用 re.match 或 re.search 成功匹配时，返回的是一个匹配对象。匹配对象有以下常用方法：
#     group()：返回匹配的字符串。
#     start()：返回匹配的起始位置。
#     end()：返回匹配的结束位置。
#     span()：返回匹配的起始和结束位置的元组。

# 分组：
# 使用括号 () 可以将正则表达式分组，分组后可以通过 group(n) 获取第 n 个分组的内容。

#  贪婪匹配：正则表达式默认是贪婪匹配，即尽可能匹配更多的字符。
#  非贪婪匹配：在量词后加上 ?，表示非贪婪匹配，即尽可能匹配更少的字符。


# 使用贪婪和非贪婪两种模式来匹配 HTML 元素
import re

html = """
<div><p>www.biancheng.net</p></div>
<div><p>编程帮</p></div>
"""

# 贪婪匹配，re.S可以匹配换行符
# 创建正则表达式对象
pattern = re.compile('<div><p>.*</p></div>', re.S)
re_list = pattern.findall(html)
print(re_list)

# 非贪婪模式匹配，re.S可以匹配换行符，使用.?
pattern = re.compile('<div><p>.*?</p></div>', re.S)
re_list = pattern.findall(html)
print(re_list)

# 可以得出非贪婪模式比适合提取 HTML 信息


# 正则表达式方法中的`flags`参数
# - re.I(re.IGNORECASE)：忽略大小写。
# - re.S(re.DOTALL)：使 . 匹配任意字符，包括换行符。
# - re.M(re.MULTILINE)：多行匹配，影响 ^ 和 $ 的行为。
# - re.X(re.VERBOSE)：忽略正则表达式中的空白和注释。

pattern = r'hello'
text = 'Hello,world'
match = re.search(pattern, text, flags=re.I)
print(match.group())


# 正则匹配身份证号
res = re.match(r'^[1-9]\d{5}(19|20)\d{2}[0-9]\d{4}')