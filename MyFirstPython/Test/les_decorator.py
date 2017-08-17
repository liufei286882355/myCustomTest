#!/usr/bin/env python
# -*- coding:utf-8 -*-


#                       函数装饰器：在不改变原有的函数的基础上给函数增加特定的功能


import functools


#不带参数的decorator
def addNow(func):
    @functools.wraps(func)#如果不加入该方法，那么调用now函数的时候名称将变为now_add
    def now_add(*args, **kw):
        print 'call %s()' %func.__name__
        return func(*args, **kw)
    return now_add


#带参数的decorator则需要再多嵌套一层函数
def log(para):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print 'call %s() with %s' %(func.__name__, para)
            return func(*args, **kw)
        return wrapper
    return decorator




@addNow
def now():
    print '2017-08-16'

@log('what do you do ?')
def dosomething():
    print 'do something'

dosomething()






#演示的例子为：判断不同分数线的及格要求


def func_150(val):
    if val >= 90:
        print ('pass')
    else :
        print ('fail')

def func_100(val):
    if val >= 60:
        print ('pass')
    else:
        print ('fail')

#如果使用上面这样的方式写成的函数，作出修改的时候就需要修改两个函数，工作量非常的大，而且容易出错
#这时候使用闭包就显得非常的简便了

def setpassline(passline):
    def func(val):
        if val >= passline:
            print ('pass');
        else:
            print ('fail')
    return func

f_100 = setpassline(60)
f_150 = setpassline(90)

f_100(89)
f_150(89)



def my_sum(*args):
    return sum(args)

def my_avarge(*args):
    return sum(args)/len(args)

#上面的两个函数一个是求和，一个是求平均数，但是这两个函数都没有对参数做限制，如果参数出错，那么就容易报错不能执行
#其实两个函数对于参数的限制是一样的，这个时候我们如果要修改的话可以使用最愚蠢的办法就是做好一个然后在复制粘贴
#但是这样的效率是非常不好，如果下个需要更改就再要两个都改
















print now.__name__
now()