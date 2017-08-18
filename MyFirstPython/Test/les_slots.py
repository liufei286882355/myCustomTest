#!/usr/bin/env python
# -*- coding:utf-8 -*-


class student(object):
    pass



s = student()

s.name = 'Jhon'
s.age = 18

def log_studentinfo(self, name, age):
    print ('the student name is '+self.name+' age is '+str(self.age))

from types import MethodType
s.log_studentinfo = MethodType(log_studentinfo, s)

print s.log_studentinfo(s.name, s.age)



class men(object):
    __slots__ = ('name', 'age', 'sex')

def meninfo(self, name, age, sex):
    print self.name + 'is' + str(self.age) + str(self.sex)

men.meninfo = meninfo

jhon = men()
jhon.name = 'Jhon'
jhon.age = 25
jhon.sex = 'male'
#jhon.height = 180  #因为该属性并不在可绑定的范围内，因此不能绑定

jhon.meninfo(jhon.name, jhon.age, jhon.sex)






#       @property
#在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是没有办法检查参数，导致属性的赋值混乱不合理而且还能随便更改
#这样显然不合逻辑。为了限定属性的范围，可以通过setter的方法来设定，再通过一个getter方法来获取

#但是，setter和getter的方法的调用又略显复杂，不够直接用属性这么直接简单
#装饰器（decorator）可以给函数动态加上功能，对于类的方法，装饰器一样起作用。python内置的@property装饰器就是负责把一个方法变成属性调用的


class Teacher(object):


    #类属性
    work = '教书育人'


    @classmethod    #类方法装饰器
    def get_work(cls):
        return cls.work


    #这个就是getter的方法
    @property
    def score(self):
        return self._score

    #这个就是setter的方法
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 and value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
    #有了以上的设定，那么score就可以使用点的方式调用以及赋值了


    #如果不设定该属性的setter方法，那么该属性就是一个只读的属性，age就通过设定birth来求得的一个只读的属性
    @property
    def age(self):
        return 2017 - self._birth

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, birth):
        self._birth = birth



teacher = Teacher()
teacher.score = 99
print str(teacher.score)


teacher.birth = 1989
print str(teacher.age)

print Teacher.get_work()