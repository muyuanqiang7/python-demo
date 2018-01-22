#!/usr/local/python3
# encoding:utf-8
# filename:module.py
import sys

import fibonacci

import using__name


def command_print():
    print("command args:")
    for i in sys.argv:
        print(i)
    print("\n\npython system path is", sys.path, "\n")


def print_func(param):
    fibonacci.fib(10)
    using__name.print_name()
    print(fibonacci.fib2(10))
    print("Hello, ", param)
