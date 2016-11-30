#!/usr/bin/python
# -*- coding: utf-8 -*-


_in_list = False

my_list = ['c','java','python','node','javascript','html','css']

while True:
    my_element = raw_input('please input message:')
    if 'exit' == my_element:
        break
    for element in my_list:
        if my_element ==element:
             _in_list = True
             break
    print 'my element %s in list result is %s ' % (element,_in_list)
