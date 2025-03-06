import re

html = """
<div class="movie-item-info">
<p class="name">
<a title="你好，李焕英">你好，李焕英</a>
</p>
<p class="star">
主演：贾玲,张小斐,沈腾
</p>    
</div>
<div class="movie-item-info">
<p class="name">
<a title="刺杀，小说家">刺杀，小说家</a>
</p>
<p class="star">
主演：雷佳音,杨幂,董子健,于和伟
</p>    
</div> 
"""

# <a title="(.*?)"> 匹配 <a> 标签中的 title 属性值，即影片名称。(.*?) 是一个非贪婪匹配，确保只匹配到第一个 ">。
# .*?保证</a>之前有东西的时候能正常匹配
pattern = r'<a title="(.*?)">.*?</a>.*?<p class="star">\s*主演：(.*?)\s</p>'
matches = re.findall(pattern, html, re.DOTALL)
for matche in matches:
    print("电影名称：", matche[0])
    print("主演：",matche[1])



# 提取影片名称
name_pattern = r'<a title="(.*?)">'
names = re.findall(name_pattern, html)

# 提取主演信息
star_pattern = r'<p class="star">\s*主演：(.*?)\s*</p>'
stars = re.findall(star_pattern, html, re.DOTALL)

for i, (name, star) in enumerate(zip(names, stars), 1):
    print(f"影片 {i}:")
    print(f"名称: {name}")
    print(f"主演: {star}")
    print()