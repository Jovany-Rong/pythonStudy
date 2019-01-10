#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import os
from functools import reduce

def quadratic(a, b, c):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        raise TypeError('bad operand type')
    delta = b ** 2 - 4 * a * c
    if a == 0:
        return - c / b
    else:
        if delta < 0:
            return
        elif delta == 0:
            return - b / 2 * a
        else:
            return ((- b + math.sqrt(delta)) / 2 * a, (- b - math.sqrt(delta)) / 2 * a)

def multiple(*num):
    for x in num:
        if not isinstance(x, (int, float)):
            raise TypeError('bad operand type')
    m = 1
    for x in num:
        m *= x
    return m

def findMinAndMax(L):
    if L == []:
        return(None, None)
    min = L[0]
    max = L[0]
    for i in L:
        if min > i:
            min = i
        if max < i:
            max = i
    return (min, max)

def nameNormalize(name):
    if not isinstance(name, str):
        raise TypeError
    return name.capitalize()

def prod(L):
    def fn(a, b):
        return a * b
    return reduce(fn, L)

def createCounter():
    def f():
        i = 1
        while True:
            yield i
            i += 1
    it = f()
    def counter():
        return next(it)
    return counter