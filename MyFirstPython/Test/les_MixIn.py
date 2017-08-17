#!/usr/bin/env python
# -*- coding:utf-8 -*-






#                       多继承
#继承是面向对象编程的一个重要方式,因为通过继承,子类可以扩展父类的功能
#而多继承可以让一个子类可以同时获得多个父类的所有功能

#                       MixIn
#在设计类的继承关系时,通常,主线是单一继承下来的
#但是如果需要"混入"额外的功能,通过多继承就可以实现,这种设计通常叫MixIn

#MixIn的目的就是给一个类增加多个功能,这样,在设计类的时候,我们优先考虑通过多重继承来组合多个MixIn的功能,
#而不是设计多层次的复杂的继承关系.
#例如:Python自带了TCPServer和UDPServer这两类网络服务,而要同时服务多个用户就必须使用多进程或多线程,
#   这两种模型由forkingMixIn和ThreadingMixIn提供.通过组合,我们可以创造出合适的服务来

#例如编写一个多进程模式的TCP服务,定义如下
#class MyTCPServer(TCPServer, ForkingMixIn):
#    pass

#编写一个多线程的UDP服务,定义如下
#class MyUDPServer(UDPServer, ThreadingMixIn)
#   pass




















