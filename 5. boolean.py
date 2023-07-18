#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
# edited by Caterina Delia for practice purposes

# and   And     if both are true
# or    Or      if one is true
# not   Not     if ??
# in    Value in set
# not in    Value not in set
# is    Same object identity
# is not    Not same object identity


#
a = True
b = False
x = ( 'bear', 'bunny', 'tree', 'sky', 'rain' )
y = 'bear'


# if y in x[0]:

if y is not x[1]:
    print('expression is true')
else:
    print('expression is false')
