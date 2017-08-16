# -*- coding: utf-8 -*-
#题目：企业发放的奖金根据利润提成。
#利润(I)低于或等于10万元时，奖金可提10%；
#利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
#20万到40万之间时，高于20万元的部分，可提成5%；
#40万到60万之间时高于40万元的部分，可提成3%；
#60万到100万之间时，高于60万元的部分，可提成1.5%；
#高于100万元时，超过100万元的部分按1%提成。
#从键盘输入当月利润I，求应发放奖金总数？



def earnMoney (money):
    sum = 0

    if money <= 10:
        return '您的奖金提成为:' + str(sum)
    if money > 10 and money <= 20:
        sum = (money - 10) * 0.075 + 10 * 0.1
        return '您的奖金提成为:' + str(sum)
    if money > 20 and money <= 40:
        sum = (money - 20) * 0.05 + 10 * 0.1 + 10 * 0.075
        return  '您的奖金提成为:' + str(sum)
    if money > 40 and money <= 60:
        sum = (money - 40) * 0.03 + 20 * 0.05 + 10 * 0.175
        return '您的奖金提成为:' + str(sum)
    if money > 60 and money <= 100:
        sum = (money - 60) * 0.015 + 20 * 0.03 + 20 * 0.05 + 10 * 0.175
        return '您的奖金提成为:' + str(sum)
    if money > 100:
        sum = (money - 100) * 0.01 + 40 * 0.015 + 20 * 0.03 + 20 * 0.05 + 10 * 0.175
        return '您的奖金提成为:' + str(sum)
print  earnMoney(20000)