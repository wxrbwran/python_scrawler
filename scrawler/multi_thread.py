from threading import Thread


def fn(name):
    for i in range(100):
        print(f"fn {name}: {i}")


if "__main__" == __name__:
    t1 = Thread(target=fn, args=("t1",))
    t1.start()

    t2 = Thread(target=fn, args=("t2",))
    t2.start()
    # fn()
    # for i in range(100):
    #     print(f"main: {i}")
