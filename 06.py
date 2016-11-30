#!/usr/bin/python
# -*- coding: utf-8 -*-
_len = 0
my_list = [1,2,-1,64,2,3,5,65,55,3241,2,3,4,5]

for element in my_list:
    _len += 1

print 'mysql list len is %d' % _len

_max = 0
_min = None

for element in my_list:
    if element > _max:
        _max = element

print 'my list max is %d' % _max


for element in my_list:
    if _min == None:
       _min = element
    if _min > element:
       _min = element

print _min
