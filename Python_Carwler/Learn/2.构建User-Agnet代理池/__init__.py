# 在编写爬虫程序时，一般都会构建一个 User-Agent （用户代理）池，就是把多个浏览器的 UA 信息放进列表中，然后再从中随机选择。
# 构建用户代理池，能够避免总是使用一个 UA 来访问网站
# 因为短时间内总使用一个 UA 高频率访问的网站，可能会引起网站的警觉，从而封杀掉 IP。

# 构建代理池的方法也非常简单，在您的 Pycharm 工作目录中定义一个 ua_info.py 文件，并将各种 UA 信息以列表的形式粘贴到该文件中

# 也可以使用专门第三方的模块来随机获取浏览器 UA 信息
from fake_useragent import UserAgent

# 实例化一个对象
ua = UserAgent()

# 生成一个随机的 User-Agent 字符串
random_user_agent = ua.random
print(random_user_agent)

# 随机获取一个ie浏览器ua
print(ua.ie)
print(ua.ie)

# 随机获取一个火狐浏览器ua
print(ua.firefox)
print(ua.firefox)
