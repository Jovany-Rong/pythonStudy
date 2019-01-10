#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import os

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