#!/usr/bin/env python
# -*- coding:utf-8 -*-



#                   定制类  带有双下划綫开头和结尾的函数都是有特殊用途的


#看到类似__slots__这种形如__xxx__的变量或者函数名就要注意了,这些在Python中都是有特殊用途的

#__slots__我们已经知道怎么用了,__len__()方法我们也知道是为了能让class作用于len()函数.
#除此之外,python的class中还有许多这样有特殊用途的函数,可以帮助我们定制类


#__str__

class Student(object):
    def __init__(self, name):
        self.name = name

print (Student('Michael'))#这时候输出的结果是 <__main__.Student object at 0x1095a01d0>这样类似的
#如果我们想要打印的好看,或者打印出来自己需要的内容,那么我们就可以像以下这样做

class StudentCustom(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name:%s)' % self.name

    __repr__ = __str__


#   __repr__

print(StudentCustom('Jhon')) # 通过在类中实现了__str__()方法,返回一串我们自己定义的字符 Student object (name:Jhon)

s = StudentCustom('Kate')
s #不使用print打印的结果,而直接敲的变量,打印的结果还是前面的那样<__main__.Student object at 0x10c738210>类似这样的字符串

#解决的方式实现__repr__(),但是通常__repr__()和__str__()输出的代码是一样的.这样就可以在实现了__str__()之后,直接赋值给__repr__




#  __iter__
# __next__     python3        next   python2

#如果想要一个类被用于for...in循环,类似list或者tuple那样,就必须实现一个__iter__()方法,该方法返回一个迭代对象,然后
#python的for循环就会不断调用迭代对象的__next__()方法拿到循环的下一个值,直到遇到StopIteration错误时退出循环
#我们以斐波那契数列为列,写一个Fib类,可以用于for循环
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 #初始化两个计数器a, b

    def __iter__(self):
        return self #实列本身就是迭代对象,故返回自己

    def next(self):  #next()   2.7版本      __next__()  python之后使用
        self.a, self.b = self.b, self.a + self.b #计算下一个值
        if self.a > 100000:  #退出循环的条件
            raise StopIteration
        return self.a #返回下一个值


print(Fib())

for n in Fib():
    print(n)




#__getitem__
#Fib实例虽然能作用于for循环,看起来和list有点像,但是,把它当成list来使用还是不行,比如,取第五个元素:
# Fib()[5] 这个就不能实现

#要表现得像list那样按照下标取出元素,需要实现__getitem__()方法:
class FibItem(object):
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a+b
        return a

print(FibItem()[30])

#当然这些都是简单的实现,要正确实现一个__getitem__()还是有很多工作要做的.
#此外如果把对象看成是dict, __getitem__()的参数也可能是一个可以key的object,例如str
#与之对应的是__setitem__()方法,把对象视作list或dict来对集合赋值.最后还有一个__delitem__()方法,用于删除某个元素
#总之,通过上面的方法,我们自己定义的类表现得和python自带的list,tuple,dict没什么区别,这完全归功于动态语言的"鸭子类型"不需要强制继承某个接口



#__getattr__
#正常情况下,当我们调用类的方法或属性时,如果不存在,就会报错
#错误信息很清楚地告诉我们,没有找到某个attribute
#要避免这个错误,除了可以加上一个对应的属性外,python还有另一个机制,那就是一个__getattr__()方法,动态返回一个属性

#例如
class worker(object):
    def __init__(self):
        self.name = 'Jhon'

    def __getattr__(self, item):
        if item == 'hours':
            return 8
        if item == 'dosomething':  #也能返回一个函数
            return lambda :'搬砖'
        return AttributeError('\'Worker\' object has no attribute \'%s\''% item)

#当调用不存在的属性时,比如工作时长hours,python解析器会试图调用__getattr__(self, 'hours')来尝试获得属性,这样,我们就有机会返回hours的值

w = worker()
print w.hours

print w.dosomething()

#需要注意的是,只有在没有找到属性的情况下,才调用__getattr__,已有属性,比如name,不会再__getattr__中查找
#此外,注意到任意调用如s.abc都会返回None,这是因为我们定义的__getattr__默认返回就是None.要让class只响应特定的几个属性,我们就要按照约定
#跑出AttributeError的错误

print w.money




