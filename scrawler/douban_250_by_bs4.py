import requests
import re
import csv
import time
import random
import os
import bs4


def filter_chinese_name(name):
    print("name", name, type(name))
    return name.startswith(r'<span class="title"> / ')


def getDoubanTop250Movie():
    # url = "https://movie.douban.com/top250"
    # ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/114.0.0.0"
    # headers = {"User-Agent": ua}
    # params = {"start": (page - 1) * 25, "filter": ""}
    # res = requests.get(url, params=params, headers=headers)
    # print(os.path.dirname(__file__))
    # print(os.path.abspath(__file__))

    page_content = ""
    # with  as f:
    #     page_content = f.read()
    # print(page_content)
    page = bs4.BeautifulSoup(
        open(f"{os.path.dirname(__file__)}/douban.html"), "html.parser"
    )
    items = page.findAll("span", attrs={"class": "title"})
    name_lists = []
    for i in items:
        origin_name: str = i.string
        if origin_name.find(r"/") == 1:
            continue
        name_lists.append(origin_name)

    print("name_lists", name_lists)

    # movies = pattern.finditer(page_content)
    # f = open("movies_bs4.csv", mode="a")
    # csv_writer = csv.writer(f)
    # for i in movies:
    #     name = i.group("name")
    #     year = i.group("year").strip()
    #     score = i.group("score")
    #     total = i.group("total")
    #     csv_writer.writerow([name, year, score, total])
    # f.close()
    print("over")


if "__main__" == __name__:
    getDoubanTop250Movie()
