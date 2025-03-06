import requests   # requests在爬虫中一般用于来处理网络请求
from bs4 import BeautifulSoup
import json
import logging

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

r = requests.get('https://www.cnblogs.com/awesometang/p/11991755.html')

# 返回请求状态码，200即为请求成功
print(r.status_code)

# 返回页面代码
print(r.text)

# 对于特定类型请求，如Ajax请求返回的json数据
print(r.json())

def fetch_page(url, headers=None):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # 检查请求是否成功
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"请求失败: {e}")
        return None

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    # 这里可以根据需要提取页面中的特定信息
    print(r.text)
    title = soup.title.string if soup.title else 'No Title'
    logging.info(f"页面标题: {title}")
    return title

def save_to_file(data, filename='output.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    logging.info(f"数据已保存到 {filename}")

def main():
    url = 'https://www.cnblogs.com/awesometang/p/11991755.html'
    headers = {
        '1.User-Agent用户代理': 'Mozilla/5.Python爬虫抓取百度贴吧数据.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    html = fetch_page(url, headers)
    if html:
        title = parse_html(html)
        data = {'url': url, 'title': title}
        save_to_file(data)


if __name__ == '__main__':
    main()