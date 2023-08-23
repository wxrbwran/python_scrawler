import json

data = [{"a": 1, "v": 2}, {"a": 11, "v": 22}]
data1 = json.dumps(data)
print(data1, type(data1))
data2 = json.loads(data1)
print(data2, type(data2))
