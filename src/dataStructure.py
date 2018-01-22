#!/usr/local/bin/python3
# encoding:utf-8
from collections import deque

stack = [3, 4, 5]
print(stack.pop())

queue = deque(stack)
print(queue.popleft())

newStack = [3 * item for item in stack]
print(newStack)

vec1 = [3, 4, 5]
vec2 = [6, 7, 8]

# 列表推导式
newStack = [[x, y] for x in vec1 for y in vec2]
print(newStack)
newStack = [x * y for x in vec1 for y in vec2]
print(newStack)
newStack = [x * y for x in vec1 if x > 3 for y in vec2]
print(newStack)
newStack = [[row for i in range(5)] for row in range(5)]
print(newStack)
print(newStack[0])
arrayList = [1, 2, 3, 4, "l"]
# arrayList.sort()
print(arrayList)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]
print([[row[i] for row in matrix] for i in range(4)])

# iterator
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 使用zip遍历多个序列
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
# 反向遍历序列
for i in reversed(range(1, 10, 2)):
    print(i)
# 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值：
