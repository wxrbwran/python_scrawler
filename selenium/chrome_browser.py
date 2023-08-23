from selenium.webdriver import Chrome


def test():
    global web
    web = Chrome()
    web.get("http://wwww.baidu.com")
    print(web.title)


if "__main__" == __name__:
    test()
