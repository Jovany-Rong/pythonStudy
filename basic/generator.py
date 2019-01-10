#!/usr/bin/env python
# -*- coding: utf-8 -*-

def triangles():
    L = [1]
    while 1:
        yield L
        T = L[:]    #切片复制
        T.append(0)
        L = [T[i-1] + T[i] for i in range(len(T))]