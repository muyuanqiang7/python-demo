#!/usr/local/bin/python3
# encoding:utf-8


def catchException():
    while True:
        try:
            x = int(input("Please input a number\n"))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again   ")


def raiseException():
    raise NameError("raise Exception")


class CustomError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def useCustomException():
    try:
        raise CustomError(2 * 2)
    except CustomError as e:
        print('Custom Exception occurred, value:', e.value)
    raise CustomError("Oops")


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("devision by zero")
    else:
        print("result is {}".format(result))
    finally:
        print("executing finally clause")


divide(2, 4)
divide(2, 0)

# 预定义的清理行为
# 关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:
with open("./foo.txt") as f:
    for line in f:
        print(line, end="")
