#!/usr/bin/python
# -*- coding: utf-8 -*-

while True:
	yeas = int(raw_input('please input yeas:'))
	if yeas % 400 ==0:
		print 'good is 闰年'
	elif yeas % 4 == 0 and yeas % 100 != 0:
		print 'good is 闰年'
	else:
		print 'error'
