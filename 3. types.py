#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
# edited by Caterina Delia for practice purposes


#x = 'seven'.capitalize()
#x = 'seven'.upper()
#x = 'seven'.lower()

#x = 'seven {} {}'.format(8, 9)

#x = 'seven {1:<9} {0:>9}'.format(8, 9)  # aligns spaces
#x = 'seven {1:<09} {0:>09}'.format(8, 9)  # aligns spaces and adds 0 in the spaces


a = 8
b = 9
x = f'seven {a} {b}'
print('x is {}'.format(x))
print(type(x))


##

from decimal import *

a = Decimal('.10')
b = Decimal('.30')

x = a + a + a - b
print('x is {}'.format(x))
print(type(x))
 
###

#x = 7 > 5
#x = None

x = 'x'

print('x is {}'.format(x))
print(type(x))

if x:
    print("True")
else:
    print("False")
