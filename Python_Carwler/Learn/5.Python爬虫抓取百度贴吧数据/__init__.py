from urllib import request,parse
import time
import random
from ua_info import ua_list   # 使用自定义的ua池
import os


# 定义一个爬虫类
class TiebaSpider(object):
    # 初始化url属性
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?{}'

    # 1.请求函数，得到页面，传统三步
    def get_html(self, url):
        req = request.Request(url=url,headers={'User-Agent':random.choice(ua_list)})
        res = request.urlopen(req)
        html = res.read().decode("gbk", "ignore")
        return html

    def save_html(self, filename, html):
        with open(filename, 'w') as f:
            f.write(html)
        print(f"文件已保存到: {os.path.abspath(filename)}")

    def run(self):
        name = input('输入贴吧名：')
        begin = int(input('输入起始页：'))
        stop = int(input('输入终止页：'))
        for page in range(begin,stop+1):
            pn = (page - 1) * 50
            params={
                'kw': name,
                'pn': str(pn)
            }
            # 拼接url地址
            params = parse.urlencode(params)
            url = self.url.format(params)
            # 发请求
            html = self.get_html(url)
            # 定义名
            filename = '{}{}-{}页.html'.format(name,begin,stop)
            self.save_html(filename, html)
            #提示
            print('第%d页抓取成功'%page)
            #每爬取一个页面随机休眠1-2秒钟的时间
            time.sleep(random.randint(1,2))

#以脚本的形式启动爬虫
if __name__=='__main__':
    start=time.time()
    spider = TiebaSpider() #实例化一个对象spider
    spider.run() #调用入口函数
    end=time.time()
    #查看程序执行时间
    print('执行时间:%.2f'%(end-start))  #爬虫执行时间


'''
用面向对象的方法编写爬虫程序时，逻辑结构较为固定，总结如下
    # 程序结构
    class xxxSpider(object):
        def __init__(self):
            # 定义常用变量,比如url或计数变量等
           
        def get_html(self):
            # 获取响应内容函数,使用随机User-Agent
       
        def parse_html(self):
            # 使用正则表达式来解析页面，提取数据
       
        def write_html(self):
            # 将提取的数据按要求保存，csv、MySQL数据库等
           
        def run(self):
            # 主函数，用来控制整体逻辑
           
    if __name__ == '__main__':
        # 程序开始运行时间
        spider = xxxSpider()
        spider.run()
'''