#!/usr/local/bin/python3
# encoding:utf-8

a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])

if "H" in a:
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

if "M" not in a:
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

print(r'\n')
print(R'\n')
'''
python字符串格式化符号:
python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
'''
print("我叫 %s 今年%d岁!" % ('小明', 10))
print("我叫 %s 今年%d岁!" % ('小明', 10))
print("adadadas".count("a"))
print("adadadas".capitalize())
print(bytes.decode("中国".encode()))
print("adada1das".upper().isalpha())
print("中国".capitalize())
print("a".ljust(8))
print("a".rjust(8))

print("adada1das".lstrip("ada"))
name = "adidas"
print(name.count("a"))
print(name.split("a", 2))
print("ammKIUuY".swapcase())
a = {2: "Y"}
print("ammKIUuY".translate(a))
print("ammKIUuY".zfill(15))
a = [1, 2, 4]
b = ["a", "b", "c"]
c = [a, b]
print(max(b))
b.extend([])
b += a
b[len(b):len(b)] = a
b.clear()
print(b)
# 2D list
list_2d = [[0 for col in range(5)] for row in range(5)]
print(list_2d)
