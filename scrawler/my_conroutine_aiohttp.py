import asyncio
import aiohttp
import time
import aiofiles
from aiohttp_requests import requests


async def aio_download(url):
    # session = aiohttp.ClientSession()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            # resp.text() # 文本
            # resp.json() # json
            # resp.content.read()  # 图片
            ts = time.time()
            with open(f"./images/{ts}.jpg", "wb") as f:
                f.write(await resp.content.read())


async def aio_download_with_aiofiles(url):
    # session = aiohttp.ClientSession()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            # resp.text() # 文本
            # resp.json() # json
            # resp.content.read()  # 图片
            ts = time.time()
            async with aiofiles.open(f"./images/{ts}.jpg", "wb") as f:
                await f.write(await resp.content.read())


async def aio_download_with_aiohttp_requests(url):
    # session = aiohttp.ClientSession()
    resp = await requests.get(url)
    content = await resp.content.read()
    ts = time.time()
    async with aiofiles.open(f"./images/{ts}.jpg", "wb") as f:
        await f.write(content)


async def main():
    urls = [
        "https://img2.baidu.com/it/u=3991442762,3196638540&fm=253&fmt=auto?w=1280&h=800",
        "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fc-ssl.duitang.com%2Fuploads%2Fitem%2F202002%2F21%2F20200221162205_vZCCd.jpeg&refer=http%3A%2F%2Fc-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1695203414&t=9b35e5f64968df122dfe5842549f3fe9",
        "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fc-ssl.duitang.com%2Fuploads%2Fitem%2F202003%2F03%2F20200303232900_iuyni.thumb.1000_0.jpeg&refer=http%3A%2F%2Fc-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1695203414&t=952a44d3977b3bef7cc1ce2487e7809a",
    ]
    tasks = []
    for u in urls:
        # tasks.append(asyncio.create_task(aio_download(u)))
        # tasks.append(asyncio.create_task(aio_download_with_aiofiles(u)))
        tasks.append(asyncio.create_task(aio_download_with_aiohttp_requests(u)))

    await asyncio.wait(tasks)


if "__main__" == __name__:
    t1 = time.time()
    asyncio.run(main())
    print(f"{time.time() - t1}")  # 0.31479501724243164
