#!/usr/local/bin/python3
# encoding:utf-8
# filename:using__name.py


if __name__ == "__main__":
    print("i am come from local module")
else:
    print("i am come from an other module")


def print_name():
    print(__name__)
