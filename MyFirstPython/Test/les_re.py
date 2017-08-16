#!/usr/bin/env python
# -*- coding:utf-8 -*-



#                                           正则表达式模块
import re
import les_pianhanshu


pattern = re.compile(r'mool')
result = pattern.match('mool nisdlhsdklj')
print result.group()


print(les_pianhanshu.int2('101010101101001'))
