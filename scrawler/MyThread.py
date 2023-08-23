from threading import Thread


class MyThread(Thread):
    def run(self):
        for i in range(19):
            print(f"子线程：{i}")


if "__main__" == __name__:
    t = MyThread()
    t.start()
    for i in range(19):
        print(f"主线程：{i}")
