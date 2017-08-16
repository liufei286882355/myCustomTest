# -*- coding: utf-8 -*-

#一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？


def caclulation():
    for i in range(1, 10000):
        for j in range(1, 10000):
            if j*j -168 == i + 100 :
                return i



print caclulation()