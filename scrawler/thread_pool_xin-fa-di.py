from concurrent.futures import ThreadPoolExecutor
import time
import requests
import json
import csv


def get_xin_fa_di_price(page, writer):
    print(page)

    result = requests.post(
        "http://www.xinfadi.com.cn/getPriceData.html",
        data={"limit": 20, "current": page},
    )
    result_json = result.json()
    # print(result.json())
    lists = result_json["list"]
    # print(lists)

    for l in lists:
        writer.writerow(
            [
                l["prodCatid"],
                l["prodCat"],
                l["id"],
                l["prodName"],
                l["lowPrice"],
                l["avgPrice"],
                l["highPrice"],
                l["unitInfo"],
                l["place"],
                l["pubDate"],
            ]
        )
    # json_data = json.load(result.text)


if "__main__" == __name__:
    f = open("xin_fa_di.csv", mode="a")
    csv_writer = csv.writer(f)
    # for i in range(100):
    #     get_xin_fa_di_price(i, csv_writer)
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 100):
            t.submit(get_xin_fa_di_price, page=i, writer=csv_writer)
    f.close()
    print("over")
