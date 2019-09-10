# 爬取猫眼电影榜单

import time
import json
import requests
from pyquery import PyQuery
from multiprocessing import Pool
from requests.exceptions import RequestException


def get_one_page(url):
    # 获取一个页面
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return None
    except RequestException:
        return None
    return response.text


def pase_one_page(text):
    # 解析页面内容
    doc = PyQuery(text)
    for info in doc("dl.board-wrapper dd").items():
        dct = {}
        dct["index"] = info.find(".board-index").text()
        dct["name"] = info.find("p.name a").text()
        dct["star"] = info.find("p.star").text()
        dct["releasetime"] = info.find("p.releasetime").text()
        dct["score"] = info.find(".score").text()
        yield dct


def write_to_file(content):
    # 写入文件
    with open("data.txt", "a", encoding="utf-8") as f:
        f.write(json.dumps(content, ensure_ascii=False) + "\n")


def main(offset):
    # 程序入口
    url = "http://maoyan.com/board/4?offset={offset}"
    text = get_one_page(url.format(offset=offset))
    for item in pase_one_page(text):
        write_to_file(item)


if __name__ == "__main__":
    start = time.time()
    # 循环抓取，翻页
    # for i in range(10):
    #     main(i * 10)
    # 3.06 6.18 4.12 3.68 3.98

    # 多进程抓取，翻页
    pool = Pool()
    pool.map(main, [i * 10 for i in range(10)])
    end = time.time()
    print(end - start)
    # 0.67 0.68 0.67 1.82 0.64
