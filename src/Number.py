#!/usr/local/bin/python3
# encoding:utf-8
"""
Python 数字数据类型用于存储数值。
数据类型是不允许改变的,这就意味着如果改变数字数据类型得值，将重新分配内存空间。
shell编程环境中没问题
交互式环境中，编译器会有一个小整数池的概念，会把（-5，256）间的数预先创建好，
而当a和b超过这个范围的时候，两个变量就会指向不同的对象了，因此地址也会不一样
-5，256
Python支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。
"""
a = 5
b = 5
print(id(a))
print(id(b))

a = 1000
b = 1000
print(id(a))
print(id(b))

a = 0xA0F
print(a)
b = 0o37
print(b)
print((a > b) - (a < b))  # python2 cmp函数等价
