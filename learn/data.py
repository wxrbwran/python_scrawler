lists: list[int] = [1, 2, 3, 4, 5]

str = "12sjdaskjd21"
new_str = str.strip("12")
print(f"{str} strip(12) 后是{new_str}")

res = lists[::-1]
print("res: ", res, type(res))
res2 = lists[3:1:-2]
print("res2: ", res2)

str = "1234567"
str2 = str[::-1]
print("str2: ", str2)


def test_fn(fn):
    # def innerFn(x, y):
    #     return fn(x, y)

    # return innerFn
    return lambda x, y: fn(x, y)


def sum(x: int, y: int) -> int:
    return x + y


def mul(x, y):
    return x * y


sumFn = test_fn(sum)
mulFn = test_fn(mul)

print(sumFn(1, 2))
print(mulFn(10, 2))

hello = "hello, world, hello, world,hello, world"
l = hello.split(",", 3)
print(l, "@".join(l))
