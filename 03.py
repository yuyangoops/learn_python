#!/usr/bin/python
# -*- coding: utf-8 -*-

Money = 20000
Years = 0

while Money < 40000:
	Money = Money + Money*0.088
	Years = Years + 1

print Years,Money

