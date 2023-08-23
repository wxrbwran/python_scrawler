# https://s6.bfzycdn.com/video/bajiaolongzhong/AI%E4%BF%AE%E5%A4%8DTC/index.m3u8

# https://s6.bfzycdn.com/video/bajiaolongzhong/AI%E4%BF%AE%E5%A4%8DTC/0000013.ts
# https://s6.bfzycdn.com/video/bajiaolongzhong/AI%E4%BF%AE%E5%A4%8DTC/0000014.ts

from concurrent.futures import ThreadPoolExecutor
import time
import requests
import json
import os

local_dir_path = "./mp4/ba_jiao_long_zhong_by_thread_pool/"


def get_m3u8_file(path):
    print("path", path)
    prefix = "https://s6.bfzycdn.com/video/bajiaolongzhong/AI%E4%BF%AE%E5%A4%8DTC/"
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/114.0.0.0"
    }
    resp = requests.get(f"{prefix}{path}", headers=headers)
    # print(resp.content)
    # print(resp.content.read())
    # content = resp.content
    with open(f"{local_dir_path}{path}", mode="wb") as f:
        f.write(resp.content)


def merge_m3u8(paths):
    print("paths_str", paths)
    os.system(f"cat {paths} > {local_dir_path}/movie.mp4")
    # for p in paths:
    #     print(f"{local_dir_path}{p}")


def main():
    count = 0
    paths = []
    merge_paths = ""
    max = 100
    # thread_count = 50
    # 50个线程 100个 57s

    # thread_count = 1
    # 1个线程 100个 304s

    thread_count = 5
    # 5个线程 100个 106s

    thread_count = 15
    # 15个线程 100个 92s

    with open("./mp4/ba_jiao_long_zhong.m3u8", mode="r") as f:
        for l in f:
            l = l.strip()
            if l.startswith("#") or l.startswith("/video/adjump/"):
                continue
            count += 1
            paths.append(l)
            merge_paths += f"{local_dir_path}{l} "
            if count > max:
                break
    # with ThreadPoolExecutor(thread_count) as t:
    #     for i in range(0, max + 1):
    #         t.submit(get_m3u8_file, path=paths[i])
    f.close()
    merge_m3u8(merge_paths)
    print("over")
    pass


if "__main__" == __name__:
    t1 = time.time()
    main()
    print(f"{time.time() - t1}")
