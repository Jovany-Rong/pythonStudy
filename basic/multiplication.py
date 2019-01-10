#!/usr/bin/env python
# -*- coding: utf-8 -*-

import msvcrt
from function import multiple

print('*************Multiplication*************\n**********Coded by Jovany Rong**********\n**********All rights reserved.**********')

inpt = [1] * 1000
num = [1] * 1000

print('Please input factors with the end of "x".')

i = 1

while inpt[i - 1] != 'x':
    num[i - 1] = float(inpt[i - 1])
    inpt[i] = input('Input the #%d factor:'%(i))
    i += 1

m = multiple(*num)

print('The result is', m, '.')