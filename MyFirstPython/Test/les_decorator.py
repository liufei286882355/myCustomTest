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

print now.__name__
now()