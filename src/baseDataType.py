#!/usr/local/bin/python3
# encoding:utf-8
counter = 1000  # 整型变量
miles = 100.0  # 浮点型变量
name = "YouTube"  # 字符串变量
print(name)
# Number
a, b, c, d = 100, 100.0, True, 4 + 3j
print(type(a), type(b), type(c), type(d))
print(4 / 5)
print(name[0:1])

# String
custom = "Runnable"
print(custom)
print(custom[0:-1])
print(custom[0])
print(custom[2:5])
print(custom[2])
print(custom[2:])
print(custom * 2)
print(custom)
# list
pythonList = ["name", {"age": 26}]
print(pythonList[1])
doubleList = pythonList * 2
print(doubleList[0: -1])
print(doubleList)
print(doubleList + pythonList)
doubleList[0] = pythonList
print(doubleList)
print("-----------------------")
# Tuple
pythonTuple = ("name", 34, {"name": pythonList})
print(pythonTuple[2]["name"])
pythonTuple[2]["name"] = name
print(pythonTuple[2]["name"])
elementTuple = (20,)
print(elementTuple[0])
# Set
student = {"Tom", "Bob", "Jim", "Tom", "Jack", "Rose", 23}
print(student)
if "Rose" in student:
    print("Rose in Set")
else:
    print("Rose not in Set")

a = set("NewYork")
b = set("Tokyo")
print(a)
print(a - b)  # 差集
print(a | b)  # 并集
print(a & b)  # 交集
print(a ^ b)  # a和b中不同时存在的元素
# Dictionary
tinyDict = {"name": "muyuanqiang", "age": 27, "address": "四川成都市"}
print(tinyDict["name"])
print(tinyDict["age"])
print(tinyDict.keys())
print(tinyDict.values())
for item in tinyDict.keys():
    print(tinyDict[item])

''' 
python运算符
算数、比较、赋值、逻辑、位、成员、身份、运算符优先级
成员运算符: in not in
身份运算符: is is not
'''
print(2 ** 3)
a = 60
b = 13
print(a & b)
print(2 << 2)

print(a and b)
print(not (a and b))

a = 20
b = 20
print(bin(a))
print(a is b)
a = 0b0011
print(a)

print(4 & 3)
print(3 & 4)
print(bin(4))
print(bin(3))
