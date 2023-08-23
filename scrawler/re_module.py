import re

p = r"\d+"
pre_p = re.compile(p)
str = "ajsdalksjd12321,asmdna,msd123m,nas,dasdipoip9809"
# lists = re.findall(p, str)
lists = pre_p.findall(str)
# print(f"lists, {lists}")

it = re.finditer(p, str)

for i in it:
    print(i.group())

s = re.search(p, str)
# print(f"s, {s} \n{s.group()}")

# m 从头匹配
m = re.match(p, str)
# print(f"m, {m} \n{m.group()}")

html_str = """
<div class="jay"><span id="1">周杰伦</span></div>
<div class="jj"><span id="2">林俊杰</span></div>
<div class="jolin"><span id="3">蔡依林</span></div>
"""

pre_html = re.compile(
    r'<div class=".*?"><span id="(?P<id>.*?)">(?P<name>.*?)</span></div>'
)
# lists1 = pre_html.findall(html_str)
# print(lists1)

it1 = pre_html.finditer(html_str)
for i in it1:
    print(i.group("id"), i.group("name"))
