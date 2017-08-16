# -*- coding: utf-8 -*-

#输入某年某月某日，判断这一天是这一年的第几天？

#思路：1.根据月份求出天数
#     2.再加上输入的天数
#     3.最后验证输入的年份是否为闰年，如果为闰年的话，那么再再总数上加多一天

def caculateDay(date):
    year = date / 10000
    month = (date - year * 10000) / 100
    day = date - year * 10000 - month * 100
    sumDay = 0
    if 1 == month:
        sumDay += 0
    elif 2 == month:
        sumDay += 31
    elif 3 == month:
        sumDay += 59
    elif 4 == month:
        sumDay += 90
    elif 5 == month:
        sumDay += 120
    elif 6 == month:
        sumDay += 151
    elif 7 == month:
        sumDay += 181
    elif 8 == month:
        sumDay += 212
    elif 9 == month:
        sumDay += 243
    elif 10 == month:
        sumDay += 273
    elif 11 == month:
        sumDay += 304
    elif 12 == month:
        sumDay += 334

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        sumDay += 1

    sumDay += day

    return sumDay


print caculateDay(20171220)

