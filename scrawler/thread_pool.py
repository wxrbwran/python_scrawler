from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def fn(name):
    for i in range(100):
        print(f"{name}: {i}")


if "__main__" == __name__:
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(fn, name=f"thread {i}")
    print("over")
