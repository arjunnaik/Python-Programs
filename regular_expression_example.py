import re

text = """
Amit age is 16 Arjun age is 21
Avinash age is 17 Valu age is 47
"""
ages = re.findall(r"\d{1,3}", text)
names = re.findall(r"[A-Z][a-z]*", text)

x = 0
dic = {}
for name in names:
    dic[name] = ages[x]
    x = x + 1
print(dic)


x = re.findall("inform", "we need to inform the information")
print(x)
if re.search("inform", "we need to inform the information"):
    print("Inform is there in above sentence")


str = "we need to inform the information"
for i in re.finditer("inform", str):
    obj = i.span()
    print(obj)