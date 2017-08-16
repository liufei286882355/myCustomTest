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


#Python 内建的filter()函数用于过滤  序列
#和 map()类似,filter() 也接收一个函数和一个序列.和map()不同的是,filter()把传入的函数一次作用于每一个元素
#然后根据返回值是true 还是 false 决定保留还是丢弃该元素

def is_odd(x):
    return  x%2 == 0

odd_list = filter(is_odd, list)#提取序列中的偶数
print(odd_list)


def not_empty(s):
    return s and s.strip()

stringList = ['', 'sd', None, 'sdw', ' ', 'wg', '12']
not_emptyList = filter(not_empty, stringList)  #提取字符串中不是空的字符组成序列
print(not_emptyList)

def is_palindrome(n):
    return str(n)[::-1] == str(n)

is_palindrome_list = filter(is_palindrome, range(1, 1000))
print(is_palindrome_list)

number_list = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]

only = number_list[::-1]  #[::-1] 切片中的运用,[从当前下表:目标下标,但不包含:每多少个取一个(-1为倒叙全部取)]
print(only)


#sorted
#排序算法
#排序也是在程序中经常用到的算法,无论使用冒泡排序还是快速排序,排序的核心是比较两个元素的大小
#如果是数字,我们可以直接比较,如果是字符串或者两个dict呢?直接比较数学书的大小是没有意义的,因此比较的过程必须通过函数抽象出来

waitsortlist = [12,-41,51,42,2,-23,12,14,24,5]

sortedlist = sorted(waitsortlist)
print(sortedlist)

#可以根据特定的条件进行排序, key指定的函数作用于list的每一个元素上,并根据key函数返回的结果进行排序
abssortedlist = sorted(waitsortlist,key=abs)#绝对值排序
print(abssortedlist)





