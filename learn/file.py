file = open("text.txt", "r", encoding="UTF-8")

print(file, type(file))
# print(file.read(14))
# print(file.read())
# print(file.readlines())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

# for l in file:
#     print(l)
file.close()

with open("text.txt", "a", encoding="UTF-8") as f:
    f.write("\nhello world")
    f.flush()

with open("text.txt", "r", encoding="UTF-8") as f:
    print(f.read().count("world"))
