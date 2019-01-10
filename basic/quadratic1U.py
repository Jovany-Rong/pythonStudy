#!/usr/bin/env python
# -*- coding: utf-8 -*-

from function import quadratic

print('***Quadratic Equation with 1 Unknown****\n**********Coded by Jovany Rong**********\n**********All rights reserved.**********')

print('A quadratic equation with 1 unknown is like A*x^2+B*x+C=0.')

a, b, c = input('Please input the A, B and C separating by SPACEs:').split()

a = float(a)
b = float(b)
c = float(c)

print('The unknown X is :', quadratic(a, b, c))