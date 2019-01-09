#!/usr/bin/env python
# -*- coding: utf-8 -*-

print('********Say Hello to All********\n******Coded by Jovany Rong******\n******All rights reserved.******')

print('Please input your names in order with the end of "x":')

names=['World'] * 1000

name = ''
i = 0

while names[i] != 'x':
    i += 1
    name = input('Please input #%d name:'%(i))
    names[i] = name

for x in range(1, i):
    print('Hello, %s.'%names[x])