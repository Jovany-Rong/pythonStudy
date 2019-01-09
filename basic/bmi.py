#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import msvcrt

print('*********BMI Calculator*********\n******Coded by Jovany Rong******\n******All rights reserved.******')

os.system('pause')

name = input('Please input your name:')
height = input('Please input %s\'s height(m):'%(name))
weight = input('Please input %s\'s weight(kg):'%(name))

height = float(height)
weight = float(weight)

bmi = weight / (height ** 2)

print('%s\'s BMI is %.1f' %(name, bmi))

if bmi <= 18.5 :
    ev = 'less-weighted'
elif bmi > 18.5 and bmi <= 25 :
    ev = 'normal-weighted'
elif bmi > 25 and bmi <= 28 :
    ev = 'over-weighted'
elif bmi > 28 and bmi <= 32 :
    ev = 'fat'
else :
    ev = 'very fat'

print('%s is %s.' %(name, ev))

print('Press any key to exit. . .')

ch = msvcrt.getch()

while ch:
    os._exit(0)