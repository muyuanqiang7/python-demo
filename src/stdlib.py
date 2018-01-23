#!/usr/local/bin/python3
# encoding:utf-8
import doctest
import unittest
from datetime import date

import zlib
from timeit import Timer

now = date.today()
print(now)

# 数据压缩

s = b'witch which has which witches wrist watch'
print(len(s))

t = zlib.compress(s)
print(len(t))
print(t)
print(zlib.decompress(t))

# 性能度量
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())


# 测试模块

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)


doctest.testmod()


class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)


unittest.main()  # Calling from the command line invokes all tests
