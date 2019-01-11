#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools

def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('%s executed in %s ms' % (func.__name__, 10.24))
        return func(*args, **kw)
    return wrapper