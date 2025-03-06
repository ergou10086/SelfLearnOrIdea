# 在开始编写程序之前，首先要确定页面类型（静态页面或动态页面）
# 其次找出页面的 url 规律
# 最后通过分析网页元素结构来确定正则表达式，从而提取网页信息。

# https://www.maoyan.com/board/4?requestCode=1740619066944-169003166-3744460&offset=20
# 其中offset每翻一页就加10，(n-1)*10

'''
<dd>
                        <i class="board-index board-index-1">1</i>
    <a href="/films/1200486" title="我不是药神" class="image-link" data-act="boarditem-click" data-val="{movieId:1200486}">
      <img src="//s3.meituan.net/static-prod01/com.sankuai.movie.fe.mywww-files/image/loading_2.e3d934bf.png" alt="" class="poster-default">
      <img alt="我不是药神" class="board-img" src="https://p0.pipi.cn/mmdb/54ecde9a2c9f2a51ba06d67d795a9434b8421.jpg?imageView2/1/w/160/h/220">
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1200486" title="我不是药神" data-act="boarditem-click" data-val="{movieId:1200486}">我不是药神</a></p>
        <p class="star">
                主演：徐峥,王传君,周一围
        </p>
<p class="releasetime">上映时间：2018-07-05</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">6</i></p>
    </div>

      </div>
    </div>

                </dd>

'''


from urllib import request
import re
import time
import random
import csv
from ua_info import ua_list

class MaoyanSpider(object):
    # 初始化
    # 定义初始页面url
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'

    # 请求函数
    def get_html(self, url):
        headers = {'User-Agent': random.choice(ua_list)}
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        html = res.read().decode()
        self.parse_html(html)

    # 解析函数
    def parse_html(self, html):
        re_bds = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>'

        pattern = re.compile(re_bds, re.S)

        r_list = pattern.findall(html)
        print(r_list)
        self.save_html(r_list)

    def save_html(self, r_list):
        with open('maoyan.csv', 'a', newline='', encoding="utf-8") as f:
            writer = csv.writer(f)

            for r in r_list:
                name = r[0].strip()
                star = r[1].strip()[3:]
                time = r[2].strip()[5:15]
                L = [name, star, time]
                writer.writerow(L)
                print(name, time, star)

    def run(self):
        for offset in range(0, 11, 10):
            url = self.url.format(offset)
            self.get_html(url)
            # 生成1-2之间的浮点数
            time.sleep(random.uniform(1, 2))

if __name__ == '__main__':
    #捕捉异常错误
    try:
        spider = MaoyanSpider()
        spider.run()
    except Exception as e:
        print("错误:",e)










