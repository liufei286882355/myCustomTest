#!/usr/bin/env python
# -*- coding:utf-8 -*-



#                                           正则表达式模块
import re
import les_pianhanshu
import urllib2

pattern = re.compile(r'mool')
result = pattern.match('mool nisdlhsdklj')
print result.group()


print(les_pianhanshu.int2('101010101101001'))



def searchimage(data):
    pa = re.compile(r'src.+\.jpg')
    ss = pa.findall(data)
    if len(ss):
        return ss
    else:
        return 0
urldata = urllib2.urlopen('http://www.imooc.com/course/list?c=python')
for i in urldata:
    print searchimage(i)






