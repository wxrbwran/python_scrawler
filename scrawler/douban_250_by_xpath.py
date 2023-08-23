import os
from lxml import etree


def getDoubanTop250Movie():
    with open(f"{os.path.dirname(__file__)}/douban.html") as f:
        page_content = f.read()
    # print(page_content)
    tree = etree.HTML(page_content)
    # //*[@id="content"]/div/div[1]/ol/li
    movies = tree.xpath('//*[@id="content"]/div/div[1]/ol/li')
    for m in movies:
        print("movies", m)
        # //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]
        name = m.xpath("./div/div[2]/div[1]/a/span[1]/text()")
        print("name", name)

        # //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/div/span[2]
        score = m.xpath("./div/div[2]/div[2]/div/span[2]/text()")
        print("score", score)
        # //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/div/span[4]
        # /html/body/div[3]/div[1]/div/div[1]/ol/li[1]/div/div[2]/div[2]/div/span[4]
        total = m.xpath("./div/div[2]/div[2]/div/span[4]/text()")
        print("total", total)

    print("over")


if "__main__" == __name__:
    getDoubanTop250Movie()
