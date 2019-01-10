#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print('*****Decimal to Hex for Int*****\n******Coded by Jovany Rong******\n******All rights reserved.******')

cont = 'y'

while cont == 'y':
    inNo = input('Please input a decimal INTEGER:')
    if inNo.isdigit():
        inNo = int(inNo)
        hexNo = hex(inNo)
        print('The hex format of %d is: %s'%(inNo, hexNo)) #hex() returns string!!!!
    else:
        print('Input error! It is not a DECIMAL INTEGER.')
    cont = input('Would you like to input another integer? (y/n):')

os._exit(0)