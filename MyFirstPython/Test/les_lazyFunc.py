#!/usr/bin/env python
# -*- coding:utf-8 -*-




#在函数里返回一个函数，可以做到延迟执行函数的方法


def lazySum(list):
    inde = 5
    def sum():
        sumNum = 0
        for i in list:
            sumNum += i * inde
        return sumNum
    return sum



f = lazySum([1, 3, 5, 7, 9])
#f = sum()
f #这时候并没有执行sum()方法
f() #这时候才执行sum()方法

#以上的函数的嵌套一个函数 叫做    闭包:内部函数sum可以引用外部函数lazy_sum的参数和局部变量
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。


#但是这样的方式会一个问题出现


