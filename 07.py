#!/usr/bin/python
# -*- coding: utf-8 -*-

_my_list = raw_input('please input a lot of numbers:')
_my_list2 =  list(_my_list)

lens = 0

for x in _my_list2:
    lens = lens +  1
print lens


_max_num = None
_min_num = None

for x in _my_list2:
    if _max_num == None:
        _max_num = x
    if _min_num == None:
        _min_num = x
    if _max_num < x:
        _max_num =x
    if _min_num > x:
        _min_num = x
print '最大%s,最小%s' % (_max_num,_min_num)

#思路 1.每循环一次就+1 这样就算出来list 是len  
#     2.最大数的思路，设置最大的数为None 当判断第一次的会吧第一个值赋值，继续走 当地一个值没有第二个大的会一直赋值最大的数
#     3.最小值的思路是，第一的适合会把第一个值赋值，继续走 那个最小就赋值给最新的变量  如果大什么都不操作。。
