#!/usr/bin/env python
# -*- coding:utf-8 -*-


#map()函数接收两个参数，一个是函数，一个是Iterable(迭代器，就是列表)，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

#求平方的函数
def square(x):
    return x*x

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


#test_map = map(str, list) #一行代码即可把整个数列转为字符串
test_map = map(square, list)


print test_map



#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

from functools import reduce

def add(x, y):
    return x+y

test_reduce = reduce(add, list)

print test_reduce
print sum(list)

def fn(x, y):
    return x*10 + y

print reduce(fn, list)#把一个数字列表变成一个数字[1, 2, 3, 4, 5, 6, 7, 8, 9]  123456789


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print reduce(fn, map(char2num, '135790'))
