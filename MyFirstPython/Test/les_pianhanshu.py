#!/usr/bin/env python
# -*- coding:utf-8 -*-

#           偏函数
# Python的functools模块提供了很多有用的功能,其中一个就是偏函数(Partial function)
# 要注意,这里的偏函数和数学意义上的偏函数不一样.这里就是函数的改造,通过设定原函数参数的默认值,
#可以降低函数调用的难度.而偏函数就是这样的作用


#函数int()可以把字符串转为整数,当传入字符串时,int()函数是按十进制转换:
#print int('123')

#但int()函数还提供额外的base参数,默认值为10.如果传入base参数,就可以做N进制转换:
#print int('123', base=8) #字符串内的数字必须符合8进制的标准才能进行转换,不然报错


import functools

int2 = functools.partial(int, base = 2)#把函数int()其中的一个默认参数改为特定的值传入函数改造为一个新的函数,专门转换二进制数字字符

#print(int2('10')) #该函数如果转换的字符串不是二进制的数字字符那么会报错

#可以改造获取数列中数字最大的函数.可以改为数列中比特定的一个数字大的数据
maxwithten = functools.partial(max, 99)
maxtennumber = maxwithten(3453,345,23,42,352,35,235,23,523,523,52,5,2)
#print(maxtennumber)




#当写了一个模块的时候,希望在被相应的模块调用的时候才使用,那么可以在对应的函数所在的模块当中写入


if __name__ == '__main__':#如果不是在当前模块运行,那么下面的方法将不会执行.可用作调试当前模块的内容,
    print(int2('10')) #










