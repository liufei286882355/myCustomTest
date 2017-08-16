# -*- coding: utf-8 -*-


#乘法口诀表

def chenfabiao():
    for a in range(1, 10):
        for b in range(1, 10):
            if b >= a:
                print str(b) + '*' + str(a) + '=' + str(a*b) + '\t',
        print '\n'

    return 0


chenfabiao()
