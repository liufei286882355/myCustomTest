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
#另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行

#但是这样的方式会一个问题出现


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return  i * 3

        fs.append(f)
    return fs

f1, f2, f3 = count()
print f1()
print f2()
print f3()
#以上的调用所有的结果都是相同的， 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9



#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
#如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：

def count2():
    def f(pra):
        def g():
            return pra*pra
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f(),然后数列中传入的函数名为g
    return fs

g1, g2, g3 = count2()

print g1()
print g2()
print g3()