#!/usr/local/bin/python3
# coding=utf-8
import keyword
import  sys

print("hello, world")
print("你好,中国")
print(keyword.kwlist)

# first comment
print("Hello, world")  # second comment

if 3 > 2:
    print("TRUE")
else:
    print("FALSE")

total = 1 + 2 + 3 + \
        4 + 5
print(total)
print(r"this is an unicode string")
print(r"this is an unicode string")
print(r"中国")
# input('\n\n 按enter键退出\n') # 等待用户输入 input
if 3 > 2:
    print("3>2", end="\n")
elif 3 == 3:
    print("3==3")
else:
    print("3<2", end=" ")

# 换行与print
x = 'a'
y = 'b'

print(x)
print(y)
print('----------')
print(x, end=" ")
print(y, end="")

print("\n============python import moudle===========")
print("command args")
for i in sys.argv:
    print(i)
print("python path is:", sys.path)
