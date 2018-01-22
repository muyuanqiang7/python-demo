#!/usr/local/python3
# encoding:utf-8
# filename:module.py
import sys
import fibo


def command_print():
    print("command args:")
    for i in sys.argv:
        print(i)
    print("\n\npython system path is", sys.path, "\n")


def print_func(param):
    fibo.fib(10)
    print(fibo.fib2(10))
    print("Hello, ", param)
