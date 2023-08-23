import requests
import re
import csv
import time
import random


def getDoubanTop250Movie(page: int):
    url = "https://movie.douban.com/top250"
    ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/114.0.0.0"
    headers = {"User-Agent": ua}
    params = {"start": (page - 1) * 25, "filter": ""}
    res = requests.get(url, params=params, headers=headers)
    page_content = res.text
    res.close()

    # 解析数据
    pattern = re.compile(
        r'<li>.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp;/&nbsp;.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?<span>(?P<total>.*?)人评价</span>',
        re.S,
    )

    movies = pattern.finditer(page_content)
    f = open("movies.csv", mode="a")
    csv_writer = csv.writer(f)
    for i in movies:
        name = i.group("name")
        year = i.group("year").strip()
        score = i.group("score")
        total = i.group("total")
        csv_writer.writerow([name, year, score, total])
    f.close()
    print("over")


if "__main__" == __name__:
    for i in range(1, 11):
        print(i)
        getDoubanTop250Movie(page=i)
        time.sleep(random.randint(3, 8))
