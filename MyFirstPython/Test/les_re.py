#!/usr/bin/env python
# -*- coding:utf-8 -*-



#                                           正则表达式模块
import re


pattern = re.compile(r'mool')
result = pattern.match('mool nisdlhsdklj')
print result.group()