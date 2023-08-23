# asdasd
"""
多行注释

"""
import random


print("askdlasd")
print(1)
print(1.1)

print(type("1"))
print(type(1))
print(type(1.1))

print(int(1.1))

print(str(1.1))
print(float("1.222"))
print(int("1"))

message = "asd %d, asdasd;lk %s,lasjdasd%.2f" % (3, "asdas", 1.2)
print(message)
a = "asddasd"
b = 1
c = 2.111
print(f"wosho{a}, klasdlasd{b}, asddas {c}")


def my_len(s):
    count = 0
    for i in s:
        count += 1
    return count


print(my_len("1asdasasdasdd;las"))

a = random.randint(1, 10)
