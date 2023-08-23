# https://s6.bfzycdn.com/video/bajiaolongzhong/AI%E4%BF%AE%E5%A4%8DTC/index.m3u8

# https://s6.bfzycdn.com/video/bajiaolongzhong/AI%E4%BF%AE%E5%A4%8DTC/0000013.ts
# https://s6.bfzycdn.com/video/bajiaolongzhong/AI%E4%BF%AE%E5%A4%8DTC/0000014.ts


import asyncio
import aiohttp
import time
import aiofiles
from aiohttp_requests import requests


async def download_mp4_by_m3u8(path: str, session):
    prefix = "https://s6.bfzycdn.com/video/bajiaolongzhong/AI%E4%BF%AE%E5%A4%8DTC/"
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/114.0.0.0"
    }
    # 此处初始化session，协程下载出现空白文件较多
    # async with aiohttp.ClientSession() as session:
    async with session.get(f"{prefix}{path}", headers=headers) as resp:
        async with aiofiles.open(
            f"./mp4/ba_jiao_long_zhong_by_conroutine/{path}", "wb"
        ) as f:
            await f.write(await resp.content.read())
    # resp = await requests.get(f"{prefix}{path}", headers=headers)
    # # print("resp", resp)
    # content = await resp.content.read()
    # async with aiofiles.open(
    #     f"./mp4/ba_jiao_long_zhong_by_conroutine/{path}", mode="wb"
    # ) as f:
    #     await f.write(content)


async def download_m3u8():
    m3u8_url = (
        "https://s6.bfzycdn.com/video/bajiaolongzhong/AI%E4%BF%AE%E5%A4%8DTC/index.m3u8"
    )
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/114.0.0.0"
    }
    resp = await requests.get(m3u8_url, headers=headers)
    # print("resp", resp)
    content = await resp.content.read()
    async with aiofiles.open("./mp4/ba_jiao_long_zhong.m3u8", mode="wb") as f:
        await f.write(content)

    # await download_mp4_by_m3u8()


async def main():
    tasks = []
    count = 0
    max = 20  # 任务数20时，未出现空白文件 50及100时会出现
    # 此处初始化session，协程下载出现空白文件比较少
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open("./mp4/ba_jiao_long_zhong.m3u8", mode="r") as f:
            # await f.write(content)
            async for l in f:
                l = l.strip()
                if l.startswith("#") or l.startswith("/video/adjump/"):
                    continue
                count += 1
                # print(l)
                tasks.append(asyncio.create_task(download_mp4_by_m3u8(l, session)))
                if count > max:
                    # 100个49s
                    # 50个62s 43s
                    break

            await asyncio.wait(tasks)


if "__main__" == __name__:
    t1 = time.time()
    # asyncio.run(main())
    asyncio.run(main())
    print(f"{time.time() - t1}")
