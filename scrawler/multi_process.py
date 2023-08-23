from multiprocessing import Process
import time


def fn():
    for i in range(20):
        time.sleep(0.2)
        print(f"1子进程fn: {i}")


if "__main__" == __name__:
    t = Process(target=fn)
    t.start()
    # fn()
    for i in range(20):
        time.sleep(0.2)
        print(f"2主进程: {i}")
