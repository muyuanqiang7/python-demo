#!/usr/local/bin/python3
# encoding:utf-8
import sys

classDict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(str(classDict))
print(classDict.fromkeys(["m", "n", "l"], [3, 4, 5]))
print(str(classDict))

# 斐波那契数列
a, b = 0, 1
while b < 10:
    print(b, end=",")
    a, b = b, a + b

sequence = [1, 2, 3, 4, 5]
it = iter(sequence)
print(next(it))


# 生成器
def fibonacci(n):
    x, y, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield x
        x, y = y, x + y
        counter += 1


f = fibonacci(10)


def greeting(name):
    print("Hello, %s" % name)


greeting("world")


def area(width, height):
    return width * height


print("width=", 4, "height=", 5, "area=", area(4, 5))


def change(param):
    return param.upper()


name = "Python"
print(change(name))
print(name)

# lambda

sumFunction = lambda arg1, arg2: arg1 + arg2
print(sumFunction(2, 4))

# global nonlocal关键字

num = 1


def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)


fun1()


def outer():
    num = 10

    def inner():
        nonlocal num  # nonlocal关键字声明
        num = 100
        print(num)

    inner()
    print(num)


outer()
