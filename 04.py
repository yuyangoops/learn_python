#!/usr/bin/python
# -*- coding: utf-8 -*-

lists = [9999999991,2,3,4,2,1,1,1,3,123,12,312,3,123,12,31,23,4,4,5555,6,211,1231233,2,3222222]
max_number = 0
max_number1 = 0

for x in lists:
    if x > max_number:
       max_number = x
for y in lists:
    if y  ==  max_number:
        continue
    elif y > max_number1:
        max_number1 = y
print max_number,max_number1

##思路： 首先要把第一个最大的值算出来，大致如下：
##             一、定义最大数起始为0，for循环当 x 小于0 那么 就让 max_number = x  以此类推 这样就会算出来list 里面最大的数 如果大于x什么也不做~~~
##             二、算出了最大的值，接下来 在定义个第二大的数，首先也是循环原来的list  如果 y 等于 最大的数也就是max_number 就什么也不做 一直循环
##             三、按照上面的继续赋值除 max_number外 最大的数  然后打印出来 2016年11月29日                  







