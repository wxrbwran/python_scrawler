import asyncio
import time


async def fn1():
    print(1)
    # time.sleep(3) # 造成阻塞
    await asyncio.sleep(3)
    print(1)


async def fn2():
    print(2)
    # time.sleep(4)
    await asyncio.sleep(4)
    print(2)


async def fn3():
    print(3)
    # time.sleep(5)
    await asyncio.sleep(2)
    print(3)


# if "__main__" == __name__:
#     f1 = fn1()
#     f2 = fn2()
#     f3 = fn3()

#     # asyncio.run(f1)
#     t1 = time.time()

#     tasks = [f1, f2, f3]
#     asyncio.run(asyncio.wait(tasks))

#     print(time.time() - t1)


async def main():
    # f1 = fn1()
    # await f1
    tasks = [
        asyncio.create_task(fn1()),
        asyncio.create_task(fn2()),
        asyncio.create_task(fn3()),
    ]
    await asyncio.wait(tasks)


if "__main__" == __name__:
    t1 = time.time()
    asyncio.run(main())
    print(time.time() - t1)
